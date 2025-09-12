# MCP for Beginners: Zero to Expert 🚀

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.11.3+-green.svg)](https://github.com/ModelContextProtocol/fastmcp)
[![MCP](https://img.shields.io/badge/MCP-1.13.1+-orange.svg)](https://github.com/ModelContextProtocol/python-sdk)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![uv](https://img.shields.io/badge/uv-package%20manager-blueviolet.svg)](https://github.com/astral-sh/uv)

> A comprehensive learning journey through the Model Context Protocol (MCP) from zero to expert level. This repository provides hands-on examples, progressive tutorials, and real-world implementations.
> 
> ## ✅ Estado actual (Resumen de lo implementado)
> 
> Características ya disponibles:
> - Servidor MCP basado en FastMCP (`mcp_demo/server.py`)
> - Herramientas matemáticas: add, subtract, multiply, divide (divide devuelve 0 si b == 0 para compatibilidad segura)
> - Recursos dinámicos con plantillas URI: `greeting://{name}` y `farewell://{name}`
> - Cliente MCP asíncrono (`mcp_demo/client.py`) con:
>   - Invocación de herramientas
>   - Lectura de recursos dinámicos
>   - Manejo robusto de excepciones y cierre ordenado
> - Integración opcional con LLM (GitHub Models API: o3-mini) mediante function/tool calling
>   - Fallback automático cuando no existe token (el flujo educativo sigue funcionando)
> - Carga manual de `.env` (sin dependencias externas) para credenciales
> - Logging estructurado usando `logging` (INFO para eventos clave, DEBUG para argumentos)
> - Tipado completo + docstrings estilo Google
> - Preparado para futuras pruebas (pendiente agregar test suite)
> 
> Próximo enfoque: transición a objetivos “INTERMEDIATE”.

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

#### ✅ Objective 1: Setup & Environment.

- [x] Python environment with uv
- [x] MCP and FastMCP installation
- [x] Project structure setup
- [x] Basic dependencies management

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

# Option 1: Usar entry points (si pyproject.toml ya los define)
uv run mcp-server    # inicia el servidor (stdio)
uv run mcp-client    # ejecuta cliente de demostración

# Option 2: Ejecutar directamente los scripts
uv run python mcp_demo/server.py
uv run python mcp_demo/client.py
```

### Variables de Entorno

Se pueden definir en el entorno o en un archivo `.env` en la raíz:
- `MCP_OPENAI` o `GITHUB_TOKEN`: Token para GitHub Models API (LLM opcional)

Ejemplo (Linux/macOS):
```bash
export GITHUB_TOKEN=ghp_xxx
uv run mcp-client
```
Ejemplo (Windows PowerShell):
```powershell
$env:GITHUB_TOKEN="ghp_xxx"
uv run mcp-client
```
Si no hay token: el cliente continúa sin funciones LLM (mensaje informativo en logs).

### Project Structure

```text
mcp-for-beginners/
├── mcp_demo/
│   ├── __init__.py          # Paquete principal
│   ├── client.py            # Cliente MCP asíncrono + integración LLM opcional
│   └── server.py            # Servidor FastMCP (herramientas + recursos)
├── tests/                   # Test suite (coming soon)
├── examples/                # Advanced examples (coming soon)
├── docs/                    # Documentation (coming soon)
├── pyproject.toml          # Project configuration
├── README.md               # This file
└── LICENSE                 # MIT License
```

---

## 🎯 Current Implementation

### Available Tools

- **add(a, b)**: Addition of two numbers
- **subtract(a, b)**: Subtraction of two numbers
- **multiply(a, b)**: Multiplication of two numbers
- **divide(a, b)**: Division with zero-handling
 
Nota: `divide(a, 0)` devuelve `0` y registra advertencia (`logger.warning`) para mantener la sesión estable y reforzar el patrón de “safe default”.

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

# LLM optional (si hay token): se intenta selección automática de herramienta
# Si no hay token: flujo continúa con mensaje en logs.
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
