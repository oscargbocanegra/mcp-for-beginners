# client.py
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
    try:
        print("🔮 Lanzando servidor MCP de horóscopo...")
        async with stdio_client(server_params) as (read, write):
            print("🟢 Conectado al servidor, creando sesión...")
            async with ClientSession(read, write) as session:
                await session.initialize()

                print("💬 Escribe tu mensaje (ejemplo: 'Dime el horóscopo de Libra').\nEscribe 'salir' para terminar.\n")

                while True:
                    user_input = input("🗣️ Tú: ")
                    if user_input.lower() in {"salir", "exit", "quit"}:
                        break

                    try:
                        parsed = await interpret_with_gpt(user_input)
                        tool = parsed["tool"]
                        args = parsed["arguments"]

                        print(f"🔧 Ejecutando {tool} con {args}...")
                        result = await session.call_tool(tool, arguments=args)
                        print("✅ Horóscopo:", result.structuredContent.get("result", "Sin respuesta"), "\n")

                    except Exception:
                        print("❌ No se pudo interpretar o ejecutar la herramienta:")
                        traceback.print_exc()
                        print()

    except Exception:
        print("❌ Error general:")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())
