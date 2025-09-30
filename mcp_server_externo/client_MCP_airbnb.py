import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import traceback

server_params = StdioServerParameters(
    command="npx",
    args=[
        "-y",
        "@openbnb/mcp-server-airbnb",
        "--ignore-robots-txt"
    ]
)

async def run():
    try:
        print("🟢 Conectando al servidor Airbnb...")
        async with stdio_client(server_params) as (read, write):
            print("🔁 Sesión iniciada. Creando sesión MCP...\n")

            async with ClientSession(read, write) as session:
                await session.initialize()

                print("🛠️ Herramientas disponibles:")
                tools = await session.list_tools()
                for t in tools.tools:
                    print(f"- {t.name}: {t.description}")
                print("\n📌 Puedes usar 'airbnb_search' por ejemplo.\n")
                #print(f"\n🔧 {tool.name}")
                #print(f"📄 Descripción: {tool.description}")
                #print(f"🧩 Input schema: {tool.inputSchema}")

                while True:
                    location = input("📍 ¿Dónde quieres buscar alojamiento?: ")
                    if location.lower() in {"salir", "exit", "quit"}:
                        break

                    try:
                        arguments = {
                            "location": location,
                            "checkin": "2025-09-10",
                            "checkout": "2025-09-15",
                            "adults": 2,
                            "ignoreRobotsText": True
                        }

                        result = await session.call_tool("airbnb_search", arguments=arguments)

                        print("🏠 Resultados:")
                        if result.structuredContent:
                            listings = result.structuredContent.get("results") or result.structuredContent
                            if listings:
                                for idx, item in enumerate(listings[:5], 1):  # Mostrar primeros 5
                                    print(f"{idx}. {item.get('name', 'Sin nombre')} - {item.get('price', {}).get('priceString', 'Sin precio')}")
                            else:
                                print("❗ No se encontraron alojamientos.")
                        else:
                            print(result.content or "❗ No se recibió respuesta estructurada.\n")

                    except Exception as e:
                        print("❌ Error al ejecutar búsqueda:")
                        traceback.print_exc()

    except Exception:
        print("❌ Error general:")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())
