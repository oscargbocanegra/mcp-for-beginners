from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Servidor de enrutamiento con herramientas")

@mcp.tool()
def get_status() -> dict:
    """Regresa el status del servidor."""
    return {"status": "Running", "version": "1.0.0"}

@mcp.tool()
def get_user_info(user_id: str) -> dict:
    """Obtiene información del usuario por ID."""
    users = {
        "1": {"name": "Amin", "role": "Profe"},
        "2": {"name": "Felipe", "role": "Course Director"},
        "3": {"name": "Agus", "role": "Course Director"},
        "4": {"name": "Jhon", "role": "Coordinador"},
    }

    return users.get(user_id, {"error": "Usuario no encontrado"})

@mcp.tool()
def calculate_square(number: int) -> dict:
    """Devuelve la raíz cuadrada de un número."""
    return {"number": number, "square": number ** 2}

if __name__ == "__main__":
    mcp.run()