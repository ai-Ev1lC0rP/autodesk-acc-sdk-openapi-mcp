import asyncio
import inspect
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from mcp import AutodeskMCPAsync  # noqa: E402


def test_async_methods_are_coroutines():
    client = AutodeskMCPAsync(base_url="https://example.com", verbose=False)
    auth_ns = client.authentication
    method = next(iter(vars(auth_ns).values()))
    assert inspect.iscoroutinefunction(method)
    asyncio.run(client.close())

def test_async_history(monkeypatch):
    async def run():
        client = AutodeskMCPAsync(base_url="https://example.com", verbose=False)

        async def fake_request(method, url, params=None, json=None, headers=None):
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
        await client.authentication.get_user_info()
        assert len(client.history) == 1
        record = client.history[0]
        assert record.operation_id == "get-user-info"
        assert record.method == "GET"
        assert record.url.endswith("/userinfo")
        assert record.status_code == 200
        assert record.description == "Retrieves information about the authenticated user."
        assert record.response_body == '{"ok": true}'
        await client.close()

    asyncio.run(run())

