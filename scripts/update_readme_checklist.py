#!/usr/bin/env python3
"""Update README endpoint checklist to reflect available OpenAPI endpoints."""
from pathlib import Path
import re
import yaml

HTTP_METHODS = {"get","post","put","delete","patch","options","head"}

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"


def collect_endpoints() -> set[str]:
    endpoints: set[str] = set()
    for spec_path in REPO_ROOT.rglob("*.yaml"):
        with spec_path.open("r") as fh:
            spec = yaml.safe_load(fh) or {}
        for api_path, methods in (spec.get("paths") or {}).items():
            for method in methods:
                if method.lower() in HTTP_METHODS:
                    endpoints.add(f"{method.upper()} {api_path}")
    return endpoints


def update_readme(endpoints: set[str]) -> None:
    pattern = re.compile(r'^- \[( |x)\] `([A-Z]+) ([^`]+)`')
    lines = README_PATH.read_text().splitlines(keepends=True)
    updated = []
    for line in lines:
        m = pattern.match(line)
        if m:
            method, path = m.group(2), m.group(3)
            key = f"{method} {path}"
            mark = 'x' if key in endpoints else ' '
            line = f"- [{mark}] `{method} {path}`\n"
        updated.append(line)
    README_PATH.write_text("".join(updated))


def main() -> None:
    endpoints = collect_endpoints()
    update_readme(endpoints)
    print(f"Updated README with {len(endpoints)} endpoints.")


if __name__ == '__main__':
    main()
