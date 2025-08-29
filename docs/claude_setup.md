# Setup Instructions (Claude)

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
2. **Instantiate the client**
   ```python
   from mcp import AutodeskMCP
   client = AutodeskMCP(token="<APS_TOKEN>")
   ```
3. **List available endpoints**
   ```python
   print(client.list_endpoints())
   ```
4. **Call an endpoint**
   ```python
   client.authentication_authorize(query={"response_type": "code"})
   ```

These steps were provided to help new contributors get started quickly with the MCP client.
