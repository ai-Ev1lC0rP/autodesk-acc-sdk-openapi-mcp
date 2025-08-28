import os
import re
import yaml
import requests

HTTP_METHODS = {"get", "post", "put", "delete", "patch", "options", "head"}

class AutodeskMCP:
    """Dynamic client that loads APS OpenAPI specs and exposes endpoints as methods."""

    def __init__(self, base_url: str = "https://developer.api.autodesk.com", token: str | None = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})
        self.endpoints: dict[str, dict] = {}
        self._load_specs()
        self._build_methods()

    def _load_specs(self) -> None:
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        for dirpath, _dirnames, filenames in os.walk(repo_root):
            for fname in filenames:
                if fname.endswith('.yaml'):
                    with open(os.path.join(dirpath, fname), 'r') as f:
                        spec = yaml.safe_load(f)
                    category = os.path.relpath(dirpath, repo_root)
                    for api_path, methods in spec.get('paths', {}).items():
                        for method, details in methods.items():
                            if method.lower() in HTTP_METHODS:
                                op_id = details.get('operationId') or f"{method}_{api_path}"
                                key = f"{category}.{op_id}"
                                self.endpoints[key] = {"method": method.upper(), "path": api_path}

    def _build_methods(self) -> None:
        for key, data in self.endpoints.items():
            func_name = self._sanitize(key)
            setattr(self, func_name, self._make_call(data["method"], data["path"]))

    def _make_call(self, method: str, path: str):
        def call(path_params: dict | None = None, query: dict | None = None, data: dict | None = None, headers: dict | None = None):
            url = self.base_url + path
            if path_params:
                url = url.format(**path_params)
            resp = self.session.request(method, url, params=query, json=data, headers=headers)
            resp.raise_for_status()
            if not resp.content:
                return None
            try:
                return resp.json()
            except ValueError:
                return resp.text
        call.__name__ = method + '_' + self._sanitize(path)
        return call

    def _sanitize(self, key: str) -> str:
        return re.sub(r'[^0-9a-zA-Z_]', '_', key)

    def list_endpoints(self) -> list[str]:
        return sorted(self.endpoints.keys())
