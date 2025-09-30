import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from mcp import AutodeskMCP  # noqa: E402


def test_sync_history(monkeypatch):
    client = AutodeskMCP(base_url="https://example.com", verbose=False)

    def fake_request(method, url, params=None, json=None, headers=None):
        class Resp:
            status_code = 200
            headers = {"Content-Type": "application/json"}
            text = '{"ok": true}'
            content = b'{"ok": true}'

            def json(self):
                return {"ok": True}

            def raise_for_status(self):
                pass

        return Resp()

    monkeypatch.setattr(client.session, "request", fake_request)
    client.authentication.get_user_info()
    assert len(client.history) == 1
    record = client.history[0]
    assert record.operation_id == "get-user-info"
    assert record.method == "GET"
    assert record.url.endswith("/userinfo")
    assert record.status_code == 200
    assert record.description == "Retrieves information about the authenticated user."
    assert record.response_body == '{"ok": true}'
