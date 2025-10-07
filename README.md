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
> - **Multiple MCP server implementations** (calculator, web search, Airtable, external services, horoscope, context management, image processing, routing)
> - **LLM integration examples** (local, dual-mode, web-based with Flask/FastAPI)
> - **Web-based MCP clients** with FastAPI and Flask
> - **Mathematical tools** with safe error handling (division by zero returns 0)
> - **Dynamic URI template resources** (`greeting://{name}`, `farewell://{name}`)
> - **Asynchronous MCP clients** with robust exception handling
> - **External API integrations**: SerpApi (web search), Airbnb, Airtable
> - **Multimodal processing**: Image brightness analysis
> - **Context management**: Mutable shared state examples
> - **Routing patterns**: Tool delegation and service routing
> - **Optional LLM integration** (GitHub Models API) through function/tool calling
> - **Structured logging** and comprehensive typing
> - **Environment variable management** (.env support)
>
> Next focus: consolidate intermediate objectives and expand test coverage.

## 📚 Learning Path Overview

This course is designed to take you from complete beginner to MCP expert through structured, hands-on learning:

```text
🎯 BEGINNER     →    🚀 INTERMEDIATE    →    💪 ADVANCED    →    🏆 EXPERT
   (Week 1-2)           (Week 3-4)            (Week 5-6)        (Week 7-8)
```

### 🎯 Current Status: **INTERMEDIATE** 🚀

**What we've accomplished:**

✅ **BEGINNER Phase Complete:**
- [x] Basic MCP server with Mathematical operations (4 tools)
- [x] Simple MCP client for server communication
- [x] FastMCP framework integration
- [x] Dynamic resources (greetings/farewells)
- [x] Error handling and logging
- [x] Professional Python code structure
- [x] Safe division by zero handling
- [x] Environment variable management (.env support)

🚀 **INTERMEDIATE Phase (In Progress):**
- [x] Advanced LLM integration (local and dual-mode)
- [x] Web-based interfaces (Flask + FastAPI)
- [x] External API integrations (SerpApi, Airbnb, Airtable)
- [x] Multiple client-server communication patterns
- [x] Horoscope server example
- [x] Context management server
- [x] Image processing with multimodal support
- [x] Routing and delegation patterns
- [ ] Comprehensive test suite
- [ ] Performance optimization
- [ ] Enhanced authentication patterns

**Next milestone:** � **ADVANCED**

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

#### ✅ Objective 3: First MCP Client.

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
| `mcp_demo/` | Server + Client | Core course implementation (BEGINNER). | Tools: add, subtract, multiply, divide (safe divide). Resources: `greeting://{name}`, `farewell://{name}` | Server: `uv run python mcp_demo/server.py`<br>Client: `uv run python mcp_demo/client.py` |
| `CalculadoraMCP/` | Server (legacy) | Earlier calculator version; historical comparison. | Tools: add, subtract, multiply, divide (raises error on divide by zero). | `uv run python CalculadoraMCP/src/server.py` |
| `mcp_server_local/` | Server | Horoscope server with zodiac predictions | Tool: `obtener_horoscopo(signo: str)` - Returns horoscope for zodiac sign | `uv run python mcp_server_local/server.py` |
| `mcp_server_context/` | Server | Mutable shared root context example. | Tools: `update_context`, `get_root_context`. | `uv run python mcp_server_context/server.py` |
| `mcp_server_images/` | FastAPI + MCP | Multimodal integration (HTTP + MCP). | Tool: add. Resource: `greeting://{name}`. HTTP endpoint: `/image/brightness` brightness analysis. | HTTP/MCP server: `uv run uvicorn mcp_server_images.server:app --reload`<br>Image test: `curl -X POST http://localhost:8000/image/brightness -F "file=@mcp_server_images/jardin.jpg"` |
| `mcp_server_route/` | Server | Informational tools and conceptual routing example. | Tools: `get_status`, `get_user_info`, `calculate_square`. | `uv run python mcp_server_route/server.py` |
| `mcp_server_route/server2.py` | Server (async routing) | Demonstrates a router delegating to external endpoints (stub). | Tool: `execute_tool` (POST to simulated endpoints). | `uv run python mcp_server_route/server2.py` (requires real endpoints for valid responses) |
| `mcp_server_web_search/` | Server (async + API) | Web search via SerpApi with multiple modes. | Async tools: `general_search`, `news_search`, `product_search`, `qna`. | 1) `.env` with `SERPAPI_KEY=...`<br>2) `uv run python mcp_server_web_search/server.py` |
| `mcp_cliente_servidor_local/LLM/` | Client + Server + LLM | Local LLM integration with MCP server | Calculator tools + GitHub Models LLM | Server: `uv run python mcp_cliente_servidor_local/LLM/server.py`<br>Client: `uv run python mcp_cliente_servidor_local/LLM/cliente.py` |
| `mcp_cliente_servidor_local/LLM_dual/` | Client + Server + LLM | Dual-mode LLM integration | Calculator tools with dual LLM support | Similar to LLM folder |
| `mcp_cliente_servidor_local/LLM_dual_web/` | Flask + MCP + LLM | Web interface for LLM-powered MCP | Web UI for calculator + LLM chat | `uv run python mcp_cliente_servidor_local/LLM_dual_web/app.py` |
| `mcp_cliente_servidor_local/TestComunication/` | Client + Server | Basic communication testing | Simple echo/test tools | Test scripts for validation |
| `mcp_server_externo/` | External Client | Airbnb MCP server integration | Client for external Airbnb MCP server via npx | `uv run python mcp_server_externo/client_MCP_airbnb.py` |
| `mcp_server_airtable/` | External Client | Airtable MCP integration | Client for Airtable operations via npx | Requires `AIRTABLE_API_KEY`, `BASEID`, `TABLEID` in .env<br>`uv run python mcp_server_airtable/client_MCP_airtable.py` |

### Execution Notes

1. **Initial setup**: Run `uv sync` at the repository root before starting any server.

2. **MCP Inspector**: To inspect stdio protocol traffic:

    ```bash
    npx @modelcontextprotocol/inspector uv run python <server_path>
    ```

3. **Key environment variables**:
    - `SERPAPI_KEY` (required for `mcp_server_web_search/`).
    - `MCP_OPENAI` or `GITHUB_TOKEN` (optional for LLM integration in `mcp_demo/client.py` and LLM examples).
    - `AIRTABLE_API_KEY`, `BASEID`, `TABLEID` (required for `mcp_server_airtable/`).

4. **Web servers**: Use `uvicorn` for FastAPI or run Flask apps directly:

    ```bash
    # FastAPI (mcp_server_images)
    uv run uvicorn mcp_server_images.server:app --reload
    
    # Flask (LLM_dual_web)
    uv run python mcp_cliente_servidor_local/LLM_dual_web/app.py
    ```

5. **Testing image brightness** (mcp_server_images):

    ```bash
    curl -X POST http://localhost:8000/image/brightness -F "file=@mcp_server_images/jardin.jpg"
    ```

6. **Legacy code**: `CalculadoraMCP/` is retained as historical material for educational comparison; may be moved to `archive/` later.

7. **External services**: `mcp_server_externo/` and `mcp_server_airtable/` use npx to launch external MCP servers, demonstrating integration with third-party services.

### Suggested Next Extensions

- Reusable generic client that can consume any server (`--path` argument).
- Parameterized tests iterating over all tools (schema + response validation).
- Unified logging patterns and server naming conventions.
- Script launcher: `uv run python tools/run_server.py --name web-search`.

### Project Categories

**🎯 Beginner Projects:**

- `mcp_demo/` - Core learning path
- `mcp_cliente_servidor_local/TestComunication/` - Basic patterns

**🚀 Intermediate Projects:**

- `mcp_cliente_servidor_local/LLM/` - LLM integration
- `mcp_cliente_servidor_local/LLM_dual/` - Advanced LLM patterns
- `mcp_cliente_servidor_local/LLM_dual_web/` - Web interfaces
- `mcp_server_web_search/` - API integrations
- `mcp_server_context/` - State management
- `mcp_server_local/` - Horoscope server

**💪 Advanced Projects:**

- `mcp_server_externo/` - External service integration
- `mcp_server_airtable/` - Database operations
- `mcp_server_images/` - Multimodal processing
- `mcp_server_route/` - Routing patterns

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12+ (recommended 3.13)
- [uv](https://github.com/astral-sh/uv) package manager

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/oscargbocanegra/mcp-for-beginners.git
cd mcp-for-beginners

# Install dependencies
uv sync

# Option 1: Use entry points (if defined in pyproject.toml)
uv run mcp-server    # start server (stdio)
uv run mcp-client    # run demo client

# Option 2: Run scripts directly
uv run python mcp_demo/server.py
uv run python mcp_demo/client.py
```

### Environment Variables

Create a `.env` file at the repository root:

```env
# Required for web search
SERPAPI_KEY=your_serpapi_key_here

# Optional for LLM features
GITHUB_TOKEN=ghp_your_token_here
# or
MCP_OPENAI=your_openai_key_here

# Required for Airtable integration
AIRTABLE_API_KEY=your_airtable_key_here
BASEID=your_airtable_base_id
TABLEID=your_airtable_table_id
```

**Linux/macOS:**

```bash
export GITHUB_TOKEN=ghp_xxx
uv run mcp-client
```

**Windows PowerShell:**

```powershell
$env:GITHUB_TOKEN="ghp_xxx"
uv run mcp-client
```

### Project Structure

```text
mcp-for-beginners/
├── mcp_demo/                           # Core learning materials (BEGINNER)
│   ├── __init__.py
│   ├── client.py
│   └── server.py
├── mcp_cliente_servidor_local/         # Local server experiments (INTERMEDIATE)
│   ├── LLM/                           # Basic LLM integration
│   ├── LLM_dual/                      # Dual-mode LLM
│   ├── LLM_dual_web/                  # Web-based LLM interface (Flask)
│   └── TestComunication/              # Communication tests
├── mcp_server_web_search/             # SerpApi integration (INTERMEDIATE)
├── mcp_server_externo/                # External service clients (ADVANCED)
├── mcp_server_airtable/               # Airtable integration (ADVANCED)
├── mcp_server_context/                # Context management examples
├── mcp_server_images/                 # Multimodal processing (ADVANCED)
├── mcp_server_route/                  # Routing patterns
├── mcp_server_local/                  # Horoscope server
├── CalculadoraMCP/                    # Legacy calculator (historical)
├── tests/                             # Test suite (planned)
├── examples/                          # Additional examples (planned)
├── docs/                              # Documentation (planned)
├── .github/                           # GitHub config & Copilot instructions
├── pyproject.toml
├── README.md
└── LICENSE
```

### 📂 Directory Reference

| Path | Status | Level | Description |
|------|--------|-------|-------------|
| `mcp_demo/` | ✅ Active | Beginner | Core FastMCP server and async client with optional LLM |
| `mcp_cliente_servidor_local/LLM/` | ✅ Active | Intermediate | Local LLM integration examples |
| `mcp_cliente_servidor_local/LLM_dual/` | ✅ Active | Intermediate | Dual-mode LLM architecture |
| `mcp_cliente_servidor_local/LLM_dual_web/` | ✅ Active | Intermediate | Flask web interface for MCP+LLM |
| `mcp_cliente_servidor_local/TestComunication/` | ✅ Active | Beginner | Basic client-server communication tests |
| `mcp_server_web_search/` | ✅ Active | Intermediate | SerpApi web search integration |
| `mcp_server_externo/` | ✅ Active | Advanced | External Airbnb MCP server client |
| `mcp_server_airtable/` | ✅ Active | Advanced | Airtable database integration |
| `mcp_server_context/` | ✅ Active | Intermediate | Shared context management |
| `mcp_server_images/` | ✅ Active | Advanced | Multimodal image processing (FastAPI) |
| `mcp_server_route/` | ✅ Active | Intermediate | Routing and delegation patterns |
| `mcp_server_local/` | ✅ Active | Beginner | Horoscope zodiac predictions |
| `CalculadoraMCP/` | 📦 Legacy | Beginner | Historical calculator for comparison |
| `tests/` | 📋 Planned | All | Comprehensive test suite |
| `examples/` | 📋 Planned | All | Additional practical examples |
| `docs/` | 📋 Planned | All | Extended guides and architecture docs |
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
| `docs/` | 📋 Planned | All | Extended guides and architecture docs |

---

## 🎯 Current Implementation

### Core Features (mcp_demo/)

**Available Tools:**

- **add(a, b)**: Addition of two numbers
- **subtract(a, b)**: Subtraction of two numbers
- **multiply(a, b)**: Multiplication of two numbers
- **divide(a, b)**: Division with safe zero-handling (returns 0)

**Available Resources:**

- **greeting://{name}**: Personalized greeting messages
- **farewell://{name}**: Personalized farewell messages

### LLM Integration Examples

**Basic LLM (mcp_cliente_servidor_local/LLM/):**

- Calculator server with stdio communication
- LLM client using GitHub Models API
- Automatic tool selection and execution

**Dual LLM (mcp_cliente_servidor_local/LLM_dual/):**

- Enhanced LLM integration patterns
- Multi-mode operation support

**Web LLM (mcp_cliente_servidor_local/LLM_dual_web/):**

- Flask web interface
- Interactive chat with MCP tool access
- Real-time calculator operations via LLM

### External Integrations

**Web Search (mcp_server_web_search/):**

- General web search
- News search
- Product search
- Question & Answer mode

**Airtable (mcp_server_airtable/):**

- Database record operations
- Schema exploration
- CRUD operations via npx MCP server

**External Services (mcp_server_externo/):**

- Airbnb MCP server integration via npx
- External API consumption patterns
- Search accommodations with filters

### Additional Servers

**Horoscope (mcp_server_local/):**

- Zodiac sign predictions
- Random horoscope generation
- Spanish language responses

**Context Management (mcp_server_context/):**

- Mutable shared root context
- Dynamic context updates
- User data storage patterns

**Image Processing (mcp_server_images/):**

- FastAPI + MCP integration
- Image brightness analysis
- Multimodal HTTP endpoints

**Routing (mcp_server_route/):**

- Server status information
- User information retrieval
- Mathematical operations (square calculation)
- External endpoint delegation (server2.py)

### Example Usage

```python
# Basic server (mcp_demo/server.py)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# Basic client (mcp_demo/client.py)
result = await session.call_tool("add", {"a": 10, "b": 5})
print(f"10 + 5 = {result.content[0].text}")

# LLM integration (mcp_cliente_servidor_local/LLM/cliente.py)
from llm import chat_with_tools
response = await chat_with_tools("What is 15 plus 27?", session)
print(response)  # LLM uses add tool automatically

# Web interface (mcp_cliente_servidor_local/LLM_dual_web/app.py)
# Visit http://localhost:5000 for interactive chat
```

---

## 📖 Learning Resources

### Official Documentation

- [Model Context Protocol Specification](https://modelcontextprotocol.io/docs)
- [FastMCP Documentation](https://github.com/ModelContextProtocol/fastmcp)
- [Python MCP SDK](https://github.com/ModelContextProtocol/python-sdk)

### Community

- [MCP Discord](https://discord.gg/mcp) - Real-time help and discussions
- [GitHub Discussions](https://github.com/ModelContextProtocol/python-sdk/discussions)
- [Stack Overflow #mcp](https://stackoverflow.com/questions/tagged/mcp)

### Additional Resources

- [SerpApi Documentation](https://serpapi.com/search-api) - Web search integration
- [Airtable API](https://airtable.com/developers/web/api/introduction) - Database operations
- [GitHub Models](https://github.com/marketplace/models) - LLM integration

---

## 🤝 Contributing

We welcome contributions at any level!

- 🎯 **Beginner**: Report bugs, suggest improvements, fix typos
- 🚀 **Intermediate**: Add examples, improve documentation, create tutorials
- 💪 **Advanced**: Contribute features, optimizations, integrations
- 🏆 **Expert**: Lead architecture, mentor others, review PRs

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines (coming soon).

---

## 📅 Weekly Progress Tracking

| Week | Level | Focus Area | Status |
|------|--------|------------|---------|
| 1-2  | 🎯 Beginner | MCP Foundations | ✅ COMPLETE |
| 3-4  | 🚀 Intermediate | Real-world Apps | 🔄 IN PROGRESS |
| 5-6  | 💪 Advanced | Production Systems | 📋 PLANNED |
| 7-8  | 🏆 Expert | Innovation & Leadership | 📋 PLANNED |

### Recent Milestones

**Week 3-4 Achievements:**

- ✅ LLM integration (3 implementation patterns)
- ✅ Web interface with Flask
- ✅ External API integrations (SerpApi, Airtable, Airbnb)
- ✅ Multiple client-server communication patterns
- ✅ Horoscope server implementation
- ✅ Context management examples
- ✅ Image processing with FastAPI
- ✅ Routing and delegation patterns
- 🔄 Test suite development (in progress)

---

## 🔮 Upcoming Features

### Short-term (Next 2 weeks)

- [ ] Comprehensive test suite (pytest + coverage)
- [ ] Performance benchmarking
- [ ] Enhanced error handling patterns
- [ ] Rate limiting implementation
- [ ] Caching strategies

### Mid-term (Weeks 5-6)

- [ ] Docker containerization
- [ ] Multi-server orchestration
- [ ] Plugin system architecture
- [ ] Monitoring and observability
- [ ] Production deployment guide

### Long-term (Weeks 7-8)

- [ ] Kubernetes deployment
- [ ] CI/CD pipelines
- [ ] Advanced AI integrations (RAG, Vector DB)
- [ ] Community contribution templates
- [ ] Conference-ready presentations

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Anthropic](https://anthropic.com) for the Model Context Protocol specification
- [FastMCP](https://github.com/ModelContextProtocol/fastmcp) team for the excellent framework
- The Python MCP community for continuous innovation
- [SerpApi](https://serpapi.com) for web search capabilities
- [Airtable](https://airtable.com) for database integration support
- All contributors and early adopters of this learning path

---

**Ready to master MCP? Let's build something amazing together!** 🚀

*Last updated: October 6, 2025*
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
