import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
import traceback
import os
from dotenv import load_dotenv

# Configura tu API Key
load_dotenv()
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
BASEID = os.getenv("BASEID")
TABLEID = os.getenv("TABLEID")

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
                print("\n💬 Escribe 'salir' para terminar.\n")

                while True:
                    actividad = input("📌 ¿Qué actividad deseas buscar?: ")
                    if actividad.lower() in {"salir", "exit", "quit"}:
                        break

                    try:
                        result = await session.call_tool("search_records", arguments={
                            "baseId": BASEID,
                            "tableId": TABLEID,
                            "searchTerm": actividad,
                            "maxRecords": 5
                        })

                        print("📄 Resultados encontrados:\n")
                        if result.structuredContent:
                            registros = result.structuredContent.get("records", [])
                            if registros:
                                for idx, rec in enumerate(registros, 1):
                                    fields = rec.get("fields", {})
                                    print(f"{idx}. {fields.get('Nombre del Servicio', 'Sin nombre')} - "
                                          f"{fields.get('Tipo', 'Sin tipo')} - "
                                          f"{fields.get('Precio (Euros)', 'Sin precio')}€ - "
                                          f"{fields.get('Disponibilidad', 'Sin disponibilidad')}")
                            else:
                                print("❗ No se encontraron registros para esa actividad.")
                        else:
                            print(result.content or "❗ No se recibió respuesta estructurada.\n")

                    except Exception:
                        print("❌ Error al buscar actividad:")
                        traceback.print_exc()

    except Exception:
        print("❌ Error general:")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())