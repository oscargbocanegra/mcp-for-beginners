import asyncio
import traceback
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from llm import interpret_with_gpt

server_params = StdioServerParameters(
    command="python",
    args=["server.py"]  # Ejecuta el servidor del horóscopo
)

async def run():
    try:
        print("🔮 Cliente de Horóscopo conectado al LLM y servidor MCP...")
        async with stdio_client(server_params) as (read, write):
            print("🟢 Servidor MCP conectado. Iniciando sesión...")
            async with ClientSession(read, write) as session:
                await session.initialize()

                print("💬 Puedes escribir tu mensaje. Ejemplo: 'Dime el horóscopo de Libra' o '¿Quién fue Nikola Tesla?'.")
                print("Escribe 'salir' para terminar.\n")

                while True:
                    user_input = input("🗣️ Tú: ")
                    if user_input.lower() in {"salir", "exit", "quit"}:
                        break

                    try:
                        parsed = await interpret_with_gpt(user_input)

                        # Si el modelo indica usar una herramienta
                        if isinstance(parsed, dict) and "tool" in parsed:
                            tool = parsed["tool"]
                            args = parsed.get("arguments", {})
                            print(f"🔧 Ejecutando {tool} con {args}...")

                            result = await session.call_tool(tool, arguments=args)

                            # Manejo del contenido del servidor MCP
                            final_text = None
                            if hasattr(result, "structuredContent") and isinstance(result.structuredContent, dict):
                                final_text = (
                                    result.structuredContent.get("result")
                                    or result.structuredContent.get("text")
                                    or str(result.structuredContent)
                                )
                            else:
                                final_text = getattr(result, "content", str(result))

                            print("✅ Horóscopo:", final_text, "\n")

                        # Si es respuesta normal del modelo (chat libre)
                        elif isinstance(parsed, dict) and "response" in parsed:
                            print("💬", parsed["response"], "\n")

                        # Si es texto sin JSON
                        elif isinstance(parsed, str):
                            print("💬", parsed, "\n")

                        else:
                            print("⚠️ Respuesta inesperada:", parsed, "\n")

                    except Exception:
                        print("❌ Error durante la interacción:")
                        traceback.print_exc()
                        print()

    except Exception:
        print("❌ Error general:")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())
