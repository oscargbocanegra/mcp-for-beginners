# MCP for Beginners: Zero to Expert 🚀

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.11.3+-green.svg)](https://github.com/ModelContextProtocol/fastmcp)
[![MCP](https://img.shields.io/badge/MCP-1.13.1+-orange.svg)](https://github.com/ModelContextProtocol/python-sdk)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![uv](https://img.shields.io/badge/uv-package%20manager-blueviolet.svg)](https://github.com/astral-sh/uv)

> A comprehensive learning journey through the Model Context Protocol (MCP) from zero to expert level. This repository provides hands-on examples, progressive tutorials, and real-world implementations.
> 
> ## ✅ Current Implementation Summary
>
> Features already available:
>
> - MCP server based on FastMCP (`mcp_demo/server.py`)
> - Mathematical tools: add, subtract, multiply, divide (divide returns 0 if b == 0 as a safe compatibility fallback)
> - Dynamic URI template resources: `greeting://{name}` and `farewell://{name}`
> - Asynchronous MCP client (`mcp_demo/client.py`) with:
>   - Tool invocation
>   - Dynamic resource reading
>   - Robust exception handling and orderly shutdown
> - Optional LLM integration (GitHub Models API: o3-mini) through function/tool calling
>   - Automatic fallback when no token is present (learning flow still works)
> - Manual `.env` loading (no external dependencies) for credentials
> - Structured logging using `logging` (INFO for key events, DEBUG for arguments)
> - Full typing + Google style docstrings
> - Prepared for future tests (test suite pending)
>
> Next focus: transition toward INTERMEDIATE objectives.

## 📚 Learning Path Overview

This course is designed to take you from complete beginner to MCP expert through structured, hands-on learning:

```text
🎯 BEGINNER     →    🚀 INTERMEDIATE    →    💪 ADVANCED    →    🏆 EXPERT
   (Week 1-2)           (Week 3-4)            (Week 5-6)        (Week 7-8)
```

### 🎯 Current Status: **BEGINNER** ✅

**What we've accomplished:**

- [x] Basic MCP server with **Mathematical operations**: 4 tools
- [x] Simple MCP client for server communication
- [x] FastMCP framework integration
- [x] **Dynamic resources**: 2 resources (greetings/farewells)
- [x] Error handling and logging
- [x] Professional Python code structure
- [x] Requirements.txt for easy installation
- [x] Fallback LLM (operación sin token)
- [x] Manejo seguro división por cero (divide → 0 si b == 0)
- [x] Carga de variables de entorno (.env opcional)

**Next milestone:** 🚀 **INTERMEDIATE**

---

## 🗺️ Complete Learning Roadmap

### 🎯 BEGINNER LEVEL (Weeks 1-2)

#### Foundation: Understanding MCP basics

#### ✅ Objective 1: Setup & Environment

- [x] Python environment with uv.
- [x] MCP and FastMCP installation.
- [x] Project structure setup.
- [x] Basic dependencies management.

#### ✅ Objective 2: First MCP Server

- [x] Create basic mathematical tools
- [x] Implement resource endpoints
- [x] Server startup and stdio communication
- [x] Logging and error handling

#### ✅ Objective 3: First MCP Client

- [x] Client-server connection
- [x] Tool invocation
- [x] Resource reading
- [x] Error handling and user feedback

#### 🔄 Objective 4: Code Quality (IN PROGRESS)

- [x] PEP 8 compliance
- [x] Type annotations
- [x] Comprehensive docstrings
- [ ] Unit tests with pytest
- [ ] Integration tests
  (Plan: iniciar en la siguiente iteración para validar herramientas y recursos)

---

### 🚀 INTERMEDIATE LEVEL (Weeks 3-4)

#### Building: Real-world MCP applications

#### 📋 Objective 5: Advanced Tools

- [ ] File system operations
- [ ] HTTP API integrations
- [ ] Database connectivity
- [ ] Data processing tools
- [ ] Async tool operations

#### 📋 Objective 6: Complex Resources

- [ ] Template-based resources
- [ ] Dynamic content generation
- [ ] Resource caching strategies
- [ ] Resource metadata handling
- [ ] Multi-format resource support

#### 📋 Objective 7: Authentication & Security

- [ ] Token-based authentication
- [ ] Rate limiting implementation
- [ ] Input validation and sanitization
- [ ] Secure configuration management
- [ ] Audit logging

#### 📋 Objective 8: Performance Optimization

- [ ] Connection pooling
- [ ] Request/response caching
- [ ] Batch operations
- [ ] Memory optimization
- [ ] Performance monitoring

---

### 💪 ADVANCED LEVEL (Weeks 5-6)

#### Mastering: Production-ready systems

#### 📋 Objective 9: Multi-Server Architecture

- [ ] Server discovery mechanisms
- [ ] Load balancing strategies
- [ ] Service mesh integration
- [ ] Health check systems
- [ ] Graceful shutdown handling

#### 📋 Objective 10: Plugin System

- [ ] Dynamic tool loading
- [ ] Plugin lifecycle management
- [ ] Configuration-driven plugins
- [ ] Plugin dependency resolution
- [ ] Hot-reloading capabilities

#### 📋 Objective 11: Monitoring & Observability

- [ ] Metrics collection (Prometheus)
- [ ] Distributed tracing (OpenTelemetry)
- [ ] Structured logging
- [ ] Performance profiling
- [ ] Dashboard creation

#### 📋 Objective 12: Integration Patterns

- [ ] Webhook integrations
- [ ] Message queue consumers
- [ ] Event-driven architectures
- [ ] Stream processing
- [ ] API gateway integration

---

### 🏆 EXPERT LEVEL (Weeks 7-8)

#### Innovating: Advanced implementations

#### 📋 Objective 13: Custom Protocol Extensions

- [ ] Protocol specification extensions
- [ ] Custom message types
- [ ] Protocol versioning strategies
- [ ] Backward compatibility
- [ ] Protocol documentation

#### 📋 Objective 14: AI Integration

- [ ] LLM tool integration
- [ ] Vector database connectivity
- [ ] RAG (Retrieval Augmented Generation)
- [ ] AI model serving
- [ ] Intelligent tool routing

#### 📋 Objective 15: Cloud Deployment

- [ ] Docker containerization
- [ ] Kubernetes deployment
- [ ] CI/CD pipelines
- [ ] Infrastructure as Code
- [ ] Multi-region deployment

#### 📋 Objective 16: Community Contribution

- [ ] Open source MCP tools
- [ ] Protocol improvement proposals
- [ ] Documentation contributions
- [ ] Tutorial creation
- [ ] Conference presentations

---

## 🧩 Catalog of Included MCP Projects / Servers

This section summarizes each subproject/server in the repository, its educational purpose, and how to run it. Use it as a practical index to the MCP lab.

| Project / Folder | Type | Main Purpose | Key Tools / Resources | How to Run (examples) |
|------------------|------|--------------|-----------------------|-----------------------|
| `mcp_demo/` | Server + Client | Core course implementation (BEGINNER). | Tools: add, subtract, multiply, divide (safe divide). Resources: `greeting://{name}`, `farewell://{name}` | Server: `uv run python mcp_demo/server.py`  Client: `uv run python mcp_demo/client.py` |
| `CalculadoraMCP/` | Server (legacy) | Earlier calculator version; historical comparison. | Tools: add, subtract, multiply, divide (raises error on divide by zero). | `uv run python CalculadoraMCP/src/server.py` |
| `mcp_server_context/` | Server | Mutable shared root context example. | Tools: `update_context`, `get_root_context`. | `uv run python mcp_server_context/server.py` |
| `mcp_server_images/` | FastAPI + MCP | Multimodal integration (HTTP + MCP). | Tool: add. Resource: `greeting://{name}`. HTTP endpoint: `/image/brightness` brightness analysis. | HTTP/MCP server: `uv run uvicorn mcp_server_images.server:app --reload`  Image test: `curl -X POST http://localhost:8000/image/brightness -F "file=@mcp_server_images/jardin.jpg"` |
| `mcp_server_route/` | Server | Informational tools and conceptual routing example. | Tools: `get_status`, `get_user_info`, `calculate_square`. | `uv run python mcp_server_route/server.py` |
| `mcp_server_route/server2.py` | Server (async routing) | Demonstrates a router delegating to external endpoints (stub). | Tool: `execute_tool` (POST to simulated endpoints). | `uv run python mcp_server_route/server2.py` (requires real endpoints for valid responses) |
| `mcp_server_web_search/` | Server (async + API) | Web search via SerpApi with multiple modes. | Async tools: `general_search`, `news_search`, `product_search`, `qna`. | 1) `.env` with `SERPAPI_KEY=...`  2) `uv run python mcp_server_web_search/server.py` |

### Execution Notes

1. Run `uv sync` at the repository root before starting any server.
2. To inspect stdio protocol traffic you can use the official inspector:

    ```bash
    npx @modelcontextprotocol/inspector uv run python mcp_server_context/server.py
    ```
3. Key environment variables:
    - `SERPAPI_KEY` (required for `mcp_server_web_search/`).
    - `MCP_OPENAI` or `GITHUB_TOKEN` (optional for LLM integration in `mcp_demo/client.py`).
4. `CalculadoraMCP/` is retained as historical material; may be moved to `archive/` later.
5. `server2.py` in `mcp_server_route/` needs real endpoints (currently placeholders) for meaningful responses.

### Suggested Next Extensions

- Reusable generic client that can consume any server (`--path` argument).
- Parameterized tests iterating over all tools (schema + response validation).
- Unified logging patterns and server naming conventions.
- Script launcher: `uv run python tools/run_server.py --name web-search`.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/oscargbocanegra/mcp-for-beginners.git
cd mcp-for-beginners

# Install dependencies
uv sync

# Option 1: Use entry points (if already defined in pyproject.toml)
uv run mcp-server    # start server (stdio)
uv run mcp-client    # run demo client

# Option 2: Run scripts directly
uv run python mcp_demo/server.py
uv run python mcp_demo/client.py
```

### Environment Variables

They can be defined in your shell or a `.env` file at the repository root:

- `MCP_OPENAI` or `GITHUB_TOKEN`: Token for GitHub Models API (optional LLM)

Example (Linux/macOS):

```bash
export GITHUB_TOKEN=ghp_xxx
uv run mcp-client
```

Example (Windows PowerShell):

```powershell
$env:GITHUB_TOKEN="ghp_xxx"
uv run mcp-client
```

If no token is present: the client continues without LLM features (informational log message).

### Project Structure

```text
mcp-for-beginners/
├── mcp_demo/
│   ├── __init__.py
│   ├── client.py
│   └── server.py
├── CalculadoraMCP/          # Additional example (calculator) – earlier/teaching version
├── tests/                   # Test suite (coming soon)
├── examples/                # Advanced examples (coming soon)
├── docs/                    # Documentation (coming soon)
├── .github/                 # Config, Copilot instructions, style guides
├── pyproject.toml
├── README.md
└── LICENSE
```

### 📂 Directory Reference

| Path | Status | Description |
|------|--------|-------------|
| `mcp_demo/` | Active | Main code: FastMCP server and async client with optional LLM integration. |
| `mcp_demo/server.py` | Active | Defines math tools and dynamic resources (`greeting://`, `farewell://`). |
| `mcp_demo/client.py` | Active | MCP client: stdio connection, tool calls, resource reading, LLM fallback. |
| `CalculadoraMCP/` | Legacy / Optional | Practice folder: calculator exercises / early experiments before consolidating into `mcp_demo/`. Useful for evolution comparison. |
| `tests/` | Planned | Will contain unit (tools/resources) and integration (client-server flow) tests. |
| `examples/` | Planned | Intermediate/advanced examples: auth, caching, async tools. |
| `docs/` | Planned | Extended guides, architecture diagrams, expanded roadmap. |
| `.github/` | Active | Copilot instructions (`copilot-instructions.md`), Python style guides, future automations. |
| `pyproject.toml` | Active | Project configuration, dependencies, entry points (`mcp-server`, `mcp-client`). |
| `.env` (not versioned) | Optional | Variables: `MCP_OPENAI` or `GITHUB_TOKEN`. Loaded manually if present. |
| `README.md` | Active | Main incremental learning and reference document. |
| `LICENSE` | Active | MIT License. |

Notes:

- Initial tests will focus on: (1) arithmetic result validation, (2) divide-by-zero handling, (3) resource reading.
- Planned examples: HTTP integration, temporary storage, basic authentication.
- Future documentation will include: sequence diagram (client ↔ server), error matrix and fallback strategies.
- Note about `CalculadoraMCP/`: if kept, useful logic may gradually migrate into `mcp_demo/` and this folder will be marked historical; otherwise it may be removed after Beginner phase completion.

---

## 🎯 Current Implementation

### Available Tools

- **add(a, b)**: Addition of two numbers
- **subtract(a, b)**: Subtraction of two numbers
- **multiply(a, b)**: Multiplication of two numbers
- **divide(a, b)**: Division with zero-handling
 
Note: `divide(a, 0)` returns `0` and logs a warning (`logger.warning`) to keep the session stable and reinforce the "safe default" pattern.

### Available Resources

- **greeting://{name}**: Personalized greeting messages
- **farewell://{name}**: Personalized farewell messages

### Example Usage

```python
# Server side (mcp_demo/server.py)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def divide(a: int, b: int) -> int:
    """Divide two integers. Returns 0 if b == 0 (safe fallback)."""
    if b == 0:
        return 0
    return a // b

# Resource example
@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    return f"Hello, {name}!"

# Client side (mcp_demo/client.py)  
result = await session.call_tool("add", {"a": 10, "b": 5})
print(f"10 + 5 = {result.content[0].text}")

greet = await session.read_resource("greeting://Alice")
print(greet.content[0].text)  # -> Hello, Alice!

# Optional LLM (if token present): attempts automatic tool selection
# If no token: flow continues with informational log message.
```

---

## 📖 Learning Resources

### Official Documentation

- [Model Context Protocol Specification](https://modelcontextprotocol.io/docs)
- [FastMCP Documentation](https://github.com/ModelContextProtocol/fastmcp)
- [Python MCP SDK](https://github.com/ModelContextProtocol/python-sdk)

### Community

- [MCP Discord](https://discord.gg/mcp) (Join for real-time help)
- [GitHub Discussions](https://github.com/ModelContextProtocol/python-sdk/discussions)
- [Stack Overflow #mcp](https://stackoverflow.com/questions/tagged/mcp)

---

## 🤝 Contributing

We welcome contributions at any level! Whether you're:

- 🎯 **Beginner**: Report bugs, suggest improvements
- 🚀 **Intermediate**: Add examples, improve documentation
- 💪 **Advanced**: Contribute advanced features, optimizations
- 🏆 **Expert**: Lead architectural decisions, mentor others

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📅 Weekly Progress Tracking

| Week | Level | Focus Area | Status |
|------|--------|------------|---------|
| 1-2  | 🎯 Beginner | MCP Foundations | ✅ COMPLETE |
| 3-4  | 🚀 Intermediate | Real-world Apps | 📋 PLANNED |
| 5-6  | 💪 Advanced | Production Systems | 📋 PLANNED |
| 7-8  | 🏆 Expert | Innovation & Leadership | 📋 PLANNED |

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Anthropic](https://anthropic.com) for the Model Context Protocol specification
- [FastMCP](https://github.com/ModelContextProtocol/fastmcp) team for the excellent framework
- The Python MCP community for continuous innovation

---

**Ready to start your MCP journey? Let's build something amazing together!** 🚀
