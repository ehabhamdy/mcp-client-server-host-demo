import _compression
import asyncio
from fastmcp import Client
from fastmcp.client.transports import PythonStdioTransport, StreamableHttpTransport

# (1)
# You have to run the server first
# client = Client("http://localhost:8000/mcp") 
# or
# transport = StreamableHttpTransport(url="http://localhost:8000/mcp")#
# client = Client(transport)

# (2)
# Or you can use the PythonStdioTransport and give it the path to the server script
# client = Client(transport=PythonStdioTransport(script_path="math_mcp.py"))
# ReferenceL https://gofastmcp.com/clients/transports#specialized-stdio-transports
# With STDIO transport, your client:
# * Starts the server as a subprocess when you connect
# * Manages the server’s lifecycle (start, stop, restart)
# * Controls the server’s environment and configuration
# * Communicates through stdin/stdout pipes
# This architecture enables powerful local integrations but requires understanding environment isolation and process management.
# Reference: https://gofastmcp.com/clients/transports#stdio-transport


# (3)
# import the mcp server and create a client (In-Memory Transpor)
from math_mcp import math_mcp
client = Client(math_mcp)

# async def test_tool(name: str):
#     async with client:
#         result = await client.call_tool("greet", {"name": name})
#         print(result)

# asyncio.run(test_tool("Ford"))

async def run():
    # 1. Create a new session - initialize the client
    # 2. List available prompts
    # 3. Retrieve a prompt based on the name
    # 4. List available resources
    # 5. Retrieve a resource based on the name
    # 6. List available tools
    # 7. Call a tool (execute the underlying function)

    async with client:
        await client.ping()

        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        print(tools)

        result = await client.call_tool("add", {"a": 1, "b": 2})
        print(result)

        prime_result = await client.read_resource("resource://primes/5")
        print(prime_result)


async def main():
    await run()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())