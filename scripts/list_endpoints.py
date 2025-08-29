import os, yaml

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, '..'))
HTTP_METHODS = {"get","post","put","delete","patch","options","head"}

def main():
    endpoints = {}
    for dirpath, dirnames, filenames in os.walk(REPO):
        for fname in filenames:
            if fname.endswith('.yaml'):
                path = os.path.join(dirpath, fname)
                with open(path) as f:
                    spec = yaml.safe_load(f)
                rel = os.path.relpath(dirpath, REPO)
                for api_path, methods in spec.get('paths', {}).items():
                    for method, details in methods.items():
                        if method.lower() in HTTP_METHODS:
                            endpoints.setdefault(rel, []).append(f"{method.upper()} {api_path}")
    for category in sorted(endpoints):
        print(f"### {category}\n")
        for item in sorted(endpoints[category]):
            print(f"- [ ] `{item}`")
        print()

if __name__ == '__main__':
    main()
