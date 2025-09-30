import logging
import os
import re
from dataclasses import dataclass
from types import SimpleNamespace

import httpx
import requests
import yaml

logger = logging.getLogger(__name__)

HTTP_METHODS = {"get", "post", "put", "delete", "patch", "options", "head"}


@dataclass
class RequestRecord:
    operation_id: str
    summary: str
    description: str
    method: str
    url: str
    path_params: dict | None
    query: dict | None
    data: dict | None
    headers: dict
    status_code: int
    response_headers: dict
    response_body: str


class _BaseMCP:
    """Common loader for APS OpenAPI specs and dynamic endpoint creation."""

    def __init__(
        self,
        session,
        base_url: str = "https://developer.api.autodesk.com",
        *,
        token: str | None = None,
        verbose: bool = True,
    ):
        self.base_url = base_url.rstrip("/")
        self.session = session
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})
        self.verbose = verbose
        if self.verbose:
            logging.basicConfig(level=logging.INFO)
        self.endpoints: dict[str, dict[str, dict]] = {}
        self.history: list[RequestRecord] = []
        self._load_specs()
        self._build_namespaces()

    def _load_specs(self) -> None:
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        for dirpath, _dirnames, filenames in os.walk(repo_root):
            for fname in filenames:
                if fname.endswith(".yaml"):
                    with open(os.path.join(dirpath, fname), "r") as f:
                        spec = yaml.safe_load(f) or {}
                    category = os.path.relpath(dirpath, repo_root)
                    for api_path, path_item in spec.get("paths", {}).items():
                        path_params = path_item.get("parameters", [])
                        for method, details in path_item.items():
                            if method.lower() in HTTP_METHODS:
                                op_id = details.get("operationId") or f"{method}_{api_path}"
                                params = path_params + details.get("parameters", [])
                                request_body = details.get("requestBody", {})
                                entry = {
                                    "method": method.upper(),
                                    "path": api_path,
                                    "summary": details.get("summary", ""),
                                    "description": details.get("description", ""),
                                    "parameters": params,
                                    "request_body": request_body.get("description", ""),
                                }
                                self.endpoints.setdefault(category, {})[op_id] = entry

    def _build_namespaces(self) -> None:
        for category, endpoints in self.endpoints.items():
            namespace = self._ensure_namespace(category)
            for op_id, data in endpoints.items():
                func_name = self._sanitize(op_id)
                setattr(
                    namespace,
                    func_name,
                    self._make_call(
                        op_id,
                        data["method"],
                        data["path"],
                        summary=data.get("summary", ""),
                        description=data.get("description", ""),
                        parameters=data.get("parameters"),
                        request_body=data.get("request_body"),
                    ),
                )

    def _ensure_namespace(self, category: str) -> SimpleNamespace:
        current = self
        for part in category.split(os.sep):
            attr = self._sanitize(part)
            if not hasattr(current, attr):
                setattr(current, attr, SimpleNamespace())
            current = getattr(current, attr)
        return current

    def _make_call(
        self,
        operation_id: str,
        method: str,
        path: str,
        *,
        summary: str = "",
        description: str = "",
        parameters: list | None = None,
        request_body: str | None = None,
    ):
        raise NotImplementedError

    def _sanitize(self, key: str) -> str:
        return re.sub(r"[^0-9a-zA-Z_]", "_", key)

    def list_endpoints(self) -> list[str]:
        items: list[str] = []
        for category, endpoints in self.endpoints.items():
            for op_id in endpoints:
                items.append(f"{category}.{op_id}")
        return sorted(items)


class AutodeskMCP(_BaseMCP):
    """Synchronous client that exposes APS APIs through dynamic namespaces."""

    def __init__(
        self,
        base_url: str = "https://developer.api.autodesk.com",
        token: str | None = None,
        verbose: bool = True,
    ):
        session = requests.Session()
        super().__init__(session, base_url, token=token, verbose=verbose)

    def _make_call(
        self,
        operation_id: str,
        method: str,
        path: str,
        *,
        summary: str = "",
        description: str = "",
        parameters: list | None = None,
        request_body: str | None = None,
    ):
        def call(
            path_params: dict | None = None,
            query: dict | None = None,
            data: dict | None = None,
            headers: dict | None = None,
        ):
            url = self.base_url + path
            if path_params:
                url = url.format(**path_params)
            req_headers = self.session.headers.copy()
            if headers:
                req_headers.update(headers)
            if self.verbose:
                logger.info("Operation: %s", operation_id)
                if summary:
                    logger.info("  summary=%s", summary)
                if description:
                    logger.info("  description=%s", description)
                logger.info("Request: %s %s", method, url)
                if path_params:
                    logger.info("  path_params=%s", path_params)
                if query:
                    logger.info("  query=%s", query)
                if data:
                    logger.info("  data=%s", data)
                if req_headers:
                    logger.info("  headers=%s", req_headers)
            resp = self.session.request(method, url, params=query, json=data, headers=req_headers)
            if self.verbose:
                logger.info("Response: %s", resp.status_code)
                logger.info("  headers=%s", dict(resp.headers))
                logger.info("  body=%s", resp.text)
            self.history.append(
                RequestRecord(
                    operation_id,
                    summary,
                    description,
                    method,
                    url,
                    path_params,
                    query,
                    data,
                    req_headers,
                    resp.status_code,
                    dict(resp.headers),
                    resp.text,
                )
            )
            resp.raise_for_status()
            if not resp.content:
                return None
            try:
                return resp.json()
            except ValueError:
                return resp.text

        call.__name__ = method.lower() + "_" + self._sanitize(path)
        doc = f"{operation_id}: {method} {path}"
        if summary or description:
            doc += f"\n\n{summary}"
            if description:
                doc += f"\n\n{description}"
        if parameters:
            doc += "\n\nParameters:\n"
            for p in parameters:
                name = p.get("name", "")
                loc = p.get("in", "")
                required = "required" if p.get("required") else "optional"
                desc = p.get("description", "")
                doc += f"- {name} ({loc}, {required}) {desc}\n"
        if request_body:
            doc += f"\nRequest Body: {request_body}\n"
        call.__doc__ = doc
        return call


class AutodeskMCPAsync(_BaseMCP):
    """Asynchronous client that mirrors :class:`AutodeskMCP` using httpx."""

    def __init__(
        self,
        base_url: str = "https://developer.api.autodesk.com",
        token: str | None = None,
        verbose: bool = True,
    ):
        session = httpx.AsyncClient()
        super().__init__(session, base_url, token=token, verbose=verbose)

    async def close(self) -> None:
        await self.session.aclose()

    def _make_call(
        self,
        operation_id: str,
        method: str,
        path: str,
        *,
        summary: str = "",
        description: str = "",
        parameters: list | None = None,
        request_body: str | None = None,
    ):
        async def call(
            path_params: dict | None = None,
            query: dict | None = None,
            data: dict | None = None,
            headers: dict | None = None,
        ):
            url = self.base_url + path
            if path_params:
                url = url.format(**path_params)
            req_headers = self.session.headers.copy()
            if headers:
                req_headers.update(headers)
            if self.verbose:
                logger.info("Operation: %s", operation_id)
                if summary:
                    logger.info("  summary=%s", summary)
                if description:
                    logger.info("  description=%s", description)
                logger.info("Request: %s %s", method, url)
                if path_params:
                    logger.info("  path_params=%s", path_params)
                if query:
                    logger.info("  query=%s", query)
                if data:
                    logger.info("  data=%s", data)
                if req_headers:
                    logger.info("  headers=%s", req_headers)
            resp = await self.session.request(method, url, params=query, json=data, headers=req_headers)
            if self.verbose:
                logger.info("Response: %s", resp.status_code)
                logger.info("  headers=%s", dict(resp.headers))
                logger.info("  body=%s", resp.text)
            self.history.append(
                RequestRecord(
                    operation_id,
                    summary,
                    description,
                    method,
                    url,
                    path_params,
                    query,
                    data,
                    req_headers,
                    resp.status_code,
                    dict(resp.headers),
                    resp.text,
                )
            )
            resp.raise_for_status()
            if not resp.content:
                return None
            try:
                return resp.json()
            except ValueError:
                return resp.text

        call.__name__ = method.lower() + "_" + self._sanitize(path)
        doc = f"{operation_id}: {method} {path}"
        if summary or description:
            doc += f"\n\n{summary}"
            if description:
                doc += f"\n\n{description}"
        if parameters:
            doc += "\n\nParameters:\n"
            for p in parameters:
                name = p.get("name", "")
                loc = p.get("in", "")
                required = "required" if p.get("required") else "optional"
                desc = p.get("description", "")
                doc += f"- {name} ({loc}, {required}) {desc}\n"
        if request_body:
            doc += f"\nRequest Body: {request_body}\n"
        call.__doc__ = doc
        return call

