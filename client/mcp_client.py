import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


# Locate the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Configure how the MCP client launches the server
server_params = StdioServerParameters(
    command=sys.executable,
    args=["-m", "backend.mcp_server"],
    cwd=str(PROJECT_ROOT),
)


async def main():
    # Start the server and establish communication
    async with stdio_client(server_params) as (read_stream, write_stream):

        # Create an MCP client session
        async with ClientSession(read_stream, write_stream) as session:

            # Initialize the MCP connection
            await session.initialize()
            print("Connected to the Python Calculator MCP server!\n")

            # Discover available tools
            tools_result = await session.list_tools()

            print("Available tools:")

            for tool in tools_result.tools:
                print(f"- {tool.name}: {tool.description}")

            # Execute a tool
            print("\nExecuting add_numbers(10, 20)...")

            result = await session.call_tool(
                "add_numbers",
                arguments={"a": 10, "b": 20},
            )

            print("\nTool result:")

            for content in result.content:
                if content.type == "text":
                    print(content.text)

            if result.isError:
                print("The tool execution returned an error.")


if __name__ == "__main__":
    asyncio.run(main())