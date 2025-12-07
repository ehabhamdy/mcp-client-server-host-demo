## MCP Server

Install the MCP server with:

```bash
fastmcp install claude-desktop --server-spec math_mcp.py:math_mcp 
```

Run the MCP inspector with:

```bash
fastmcp dev --server-spec math_mcp.py:math_mcp
```

Run server with:

```bash
fastmcp run math_mcp.py:math_mcp
```

Run server with http transport:

```bash
fastmcp run math_mcp.py:math_mcp --transport http --port 8000
```


Run client with:

```bash
python client.py
```
