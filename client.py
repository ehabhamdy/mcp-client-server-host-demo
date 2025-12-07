import authlib.integrations.base_client.framework_integration
import asyncio
from fastmcp import Client
from fastmcp.client.transports import PythonStdioTransport

# client = Client("http://localhost:8000/mcp")
client = Client(transport=PythonStdioTransport(script_path="notes.py:notes_mcp"))

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

        result = await client.call_tool("add", {"a": 1, "b": 2})
        print(result)


async def main():
    await run()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())