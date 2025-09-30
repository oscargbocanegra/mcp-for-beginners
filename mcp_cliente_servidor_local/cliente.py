import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import traceback

server_params = StdioServerParameters(
    command="uv",
    args=["run", "server.py"]
)

async def run():
    try:
        print("🔮 Iniciando servidor MCP de horóscopo...")
        async with stdio_client(server_params) as (read, write):
            print("🟢 Conectado al servidor MCP, creando sesión...")
            async with ClientSession(read, write) as session:
                await session.initialize()

                print("📦 Herramientas disponibles en el servidor:")
                tools = await session.list_tools()
                for tool in tools.tools:
                    print(f"- {tool.name}: {tool.description}")
                print("\n✨ Escribe 'salir' para terminar.\n")

                while True:
                    signo = input("♈ Introduce tu signo del zodiaco: ")
                    if signo.lower() in {"salir", "exit", "quit"}:
                        print("👋 Saliendo del cliente...")
                        break

                    try:
                        print(f"🔍 Solicitando horóscopo para: {signo.capitalize()}...\n")
                        result = await session.call_tool(
                            "obtener_horoscopo", 
                            arguments={"sign": signo}
                        )

                        print("🔮 Horóscopo de hoy:")
                        print(result.structuredContent.get("result", "❌ No se recibió respuesta"))
                        print("\n" + "-"*50 + "\n")

                    except Exception:
                        print("❌ Error al llamar a la herramienta:")
                        traceback.print_exc()

    except Exception:
        print("❌ Error general en el cliente:")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())
