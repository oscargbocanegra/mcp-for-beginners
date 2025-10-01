import asyncio
import traceback
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from llm import interpret_with_gpt

server_params = StdioServerParameters(
    command="python",
    args=["server.py"]  # Lanza el servidor del horóscopo
)

async def run():
    """Modo terminal: conversación continua"""
    try:
        print("🔮 Lanzando servidor MCP de horóscopo...")
        async with stdio_client(server_params) as (read, write):
            print("🟢 Conectado al servidor, creando sesión...")
            async with ClientSession(read, write) as session:
                await session.initialize()

                print("💬 Escribe tu mensaje. Ejemplo: 'Dime el horóscopo de Libra' o '¿Quién es Albert Einstein?'.\nEscribe 'salir' para terminar.\n")

                while True:
                    user_input = input("🗣️ Tú: ")
                    if user_input.lower() in {"salir", "exit", "quit"}:
                        break

                    try:
                        response = await process_message(session, user_input)
                        print("🤖", response, "\n")

                    except Exception:
                        print("❌ No se pudo interpretar o ejecutar la herramienta:")
                        traceback.print_exc()
                        print()

    except Exception:
        print("❌ Error general:")
        traceback.print_exc()

async def process_message(session, user_input: str) -> str:
    """
    Procesa un mensaje usando el LLM y MCP.
    """
    parsed = await interpret_with_gpt(user_input)

    # Si el modelo indica herramienta
    if isinstance(parsed, dict) and "tool" in parsed:
        tool = parsed["tool"]
        args = parsed.get("arguments", {})
        print(f"🔧 Ejecutando {tool} con {args}...")
        result = await session.call_tool(tool, arguments=args)
        return result.structuredContent.get("result", "Sin respuesta")

    # Si el modelo devuelve solo respuesta libre
    elif isinstance(parsed, dict) and "response" in parsed:
        return parsed["response"]

    # Si devuelve texto sin JSON
    elif isinstance(parsed, str):
        return parsed

    return "⚠️ Respuesta inesperada del modelo."

async def run_message(user_input: str) -> str:
    """
    Ejecuta UNA sola interacción para app web.
    """
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                return await process_message(session, user_input)

    except Exception as e:
        traceback.print_exc()
        return "❌ Error al procesar tu solicitud."

if __name__ == "__main__":
    asyncio.run(run())
