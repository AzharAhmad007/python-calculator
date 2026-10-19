import asyncio
import json
import sys
from pathlib import Path

import ollama

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_NAME = "qwen3:4b"


server_params = StdioServerParameters(
    command=sys.executable,
    args=["-m", "backend.mcp_server"],
    cwd=str(PROJECT_ROOT),
)


def convert_mcp_tools_to_ollama(mcp_tools):
    """Convert MCP tool definitions into Ollama tool definitions."""

    ollama_tools = []

    for tool in mcp_tools:
        ollama_tools.append(
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description or "",
                    "parameters": tool.inputSchema,
                },
            }
        )

    return ollama_tools


async def execute_tool(session, tool_call):
    """Execute a tool requested by the AI through the MCP server."""

    tool_name = tool_call.function.name
    arguments = tool_call.function.arguments

    print(f"\nAI selected tool: {tool_name}")
    print(f"Arguments: {arguments}")

    result = await session.call_tool(
        tool_name,
        arguments=arguments,
    )

    if result.isError:
        error_messages = [
            item.text
            for item in result.content
            if item.type == "text"
        ]
        return {
            "error": "\n".join(error_messages) or "Tool execution failed."
        }

    output = []

    for item in result.content:
        if item.type == "text":
            output.append(item.text)

    return {
        "result": "\n".join(output)
    }


async def chat_with_ai(session, ollama_tools):
    """Allow the user to interact with the AI and MCP tools."""

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful calculator assistant. "
                "When the user asks you to perform a calculation, "
                "use the available calculator tools. "
                "Do not calculate the result yourself when a tool "
                "can perform the calculation. "
                "After receiving a tool result, explain the answer "
                "clearly and concisely."
            ),
        }
    ]

    print("\nCalculator AI is ready!")
    print("Ask a calculation, or type 'exit' to quit.\n")

    while True:
        try:
            user_input = await asyncio.to_thread(
                input, "You: "
            )
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_input.strip().lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_input.strip():
            continue

        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        try:
            response = ollama.chat(
                model=MODEL_NAME,
                messages=messages,
                tools=ollama_tools,
            )

            messages.append(response.message)

            while response.message.tool_calls:
                for tool_call in response.message.tool_calls:
                    tool_result = await execute_tool(
                        session,
                        tool_call,
                    )

                    messages.append(
                        {
                            "role": "tool",
                            "tool_name": tool_call.function.name,
                            "content": json.dumps(tool_result),
                        }
                    )

                response = ollama.chat(
                    model=MODEL_NAME,
                    messages=messages,
                    tools=ollama_tools,
                )

                messages.append(response.message)

            print(f"\nAI: {response.message.content}\n")

        except Exception as exc:
            print(f"\nError: {exc}\n")


async def main():
    async with stdio_client(server_params) as (
        read_stream,
        write_stream,
    ):
        async with ClientSession(
            read_stream,
            write_stream,
        ) as session:

            await session.initialize()

            print("Connected to the Python Calculator MCP server.")

            tools_result = await session.list_tools()

            ollama_tools = convert_mcp_tools_to_ollama(
                tools_result.tools
            )

            print("\nAvailable calculator tools:")

            for tool in tools_result.tools:
                print(f"- {tool.name}: {tool.description}")

            await chat_with_ai(session, ollama_tools)


if __name__ == "__main__":
    asyncio.run(main())