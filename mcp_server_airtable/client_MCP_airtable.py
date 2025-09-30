import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
import os
import traceback
import logging
from dotenv import load_dotenv

# Initialize logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Configura tu API Key
load_dotenv()
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
BASEID = os.getenv("BASEID")
TABLEID = os.getenv("TABLEID")


# Parámetros para iniciar el servidor MCP
server_params = StdioServerParameters(
    command="npx",
    args=[
        "-y",
        "airtable-mcp-server"
    ],
    env={
        "AIRTABLE_API_KEY": AIRTABLE_API_KEY
    }
)

async def run():
    try:
        print("🟢 Conectando al servidor MCP de Airtable...")
        async with stdio_client(server_params) as (read, write):
            print("🔁 Sesión iniciada. Creando sesión MCP...\n")

            async with ClientSession(read, write) as session:
                await session.initialize()

                print("🛠️ Herramientas disponibles:")
                tools = await session.list_tools()
                for t in tools.tools:
                    print(f"- {t.name}: {t.description}")
                print("\n📌 Ejemplo: obtener registros de tu tabla.\n")

                # Ejecutar la herramienta que lista registros (ajusta al nombre real)
                try:
                    result = await session.call_tool("list_records", arguments={
                        "baseId": BASEID,
                        "tableId": TABLEID,
                        "max_records": 10
                    })

                    print("📄 Resultados:")
                    print(result.structuredContent or result.content)

                except Exception as e:
                    print("❌ Error al obtener registros:")
                    traceback.print_exc()

    except Exception:
        print("❌ Error general:")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())
