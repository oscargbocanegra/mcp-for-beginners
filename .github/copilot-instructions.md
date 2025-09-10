# Copilot Instructions for mcp-for-beginners

## Project Overview

This is a **Model Context Protocol (MCP) learning repository** focused on progressive skill building from beginner to expert. The project demonstrates MCP server/client implementations using the FastMCP framework with mathematical tools and dynamic resources.

## Architecture & Key Components

### Core Structure
- **`mcp_demo/server.py`**: FastMCP-based server with mathematical tools (`add`, `subtract`, `multiply`, `divide`) and dynamic resources (`greeting://`, `farewell://`)
- **`mcp_demo/client.py`**: Async MCP client with LLM integration (GitHub Models API) for intelligent tool calling
- **Entry points**: Defined in `pyproject.toml` as `mcp-server` and `mcp-client` commands

### MCP Communication Pattern
```python
# Server: FastMCP decorators for tools and resources
@mcp.tool()
def add(a: int, b: int) -> int: ...

@mcp.resource("greeting://{name}")
def greeting(name: str) -> str: ...

# Client: stdio connection with session management
async with stdio_client(SERVER_PARAMS) as (read, write):
    async with ClientSession(read, write) as session:
        result = await session.call_tool("add", {"a": 10, "b": 5})
```

## Development Workflows

### Environment Setup
```bash
# Use uv package manager (modern Python packaging)
uv sync                    # Install dependencies
uv run python mcp_demo/client.py  # Run client demo
```

### Server Communication
- **Protocol**: stdio (standard input/output) for local development
- **Server parameters**: `.venv/bin/python mcp_demo/server.py`
- **Error handling**: Division by zero returns 0 (legacy compatibility)

### LLM Integration
- **Provider**: GitHub Models API (o3-mini model)
- **Authentication**: `MCP_OPENAI` or `GITHUB_TOKEN` environment variables, or `.env` file
- **Tool schema conversion**: MCP tools → OpenAI function calling format
- **Graceful degradation**: Demo continues without LLM if token unavailable

## Critical Patterns

### Resource URI Templates
Dynamic resources use URI template patterns:
```python
# Server definition
@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    return f"Hello, {name}!"

# Client access
greeting_resource = await session.read_resource("greeting://Juan")
```

### Error Handling Strategy
- **Server**: Logs warnings, returns safe defaults (e.g., 0 for division by zero)
- **Client**: Comprehensive exception handling with cleanup, structured logging
- **LLM calls**: JSON parsing validation, timeout handling

### Logging Convention
- Use `logging` module (not print) with INFO level for key events
- Format: `logger.info("MCP client connected to server")`
- Debug level for tool arguments and detailed flow

## Project-Specific Considerations

### Learning Path Structure
This is a **tutorial project** with planned progression:
- Week 1-2: Current implementation (mathematical tools, basic resources)
- Week 3-4: Advanced tools, authentication, performance optimization
- Week 5-6: Multi-server architecture, monitoring
- Week 7-8: Custom protocol extensions, AI integration

### Dependencies
- **FastMCP 2.11.3+**: Server framework (simpler than vanilla MCP SDK)
- **MCP 1.13.1+**: Client library for Python
- **Python 3.12+**: Required for modern type annotations
- **OpenAI client**: Used for GitHub Models API integration

### Code Quality Standards
- Follow existing Python instructions in `.github/instructions/python.instructions.md`
- All code in English with comprehensive docstrings (Google style)
- Type annotations with `from __future__ import annotations`
- Error messages must be actionable and user-friendly

## Integration Points

### Environment Variables
- `MCP_OPENAI` or `GITHUB_TOKEN`: GitHub Models API authentication
- Custom `.env` file loading without external dependencies
- Graceful fallback when tokens unavailable

### Async Patterns
- Client uses `asyncio` with proper session management
- Resource cleanup in `finally` blocks with task cancellation
- Background task management for long-running operations

## When Contributing

1. **Maintain the learning progression**: Changes should support the tutorial nature
2. **Test with both token and no-token scenarios**: LLM integration is optional
3. **Preserve stdio communication**: Local development pattern for MCP
4. **Follow mathematical tool patterns**: Simple, well-documented operations
5. **Update README.md**: Reflect any architectural changes in the learning roadmap

## Common Gotchas

- **Server startup**: Must run from project root for relative paths to work
- **Tool arguments**: MCP expects exact JSON schema compliance
- **Resource URIs**: Template parameters must match function arguments exactly
- **LLM integration**: JSON parsing can fail; always validate tool call arguments
