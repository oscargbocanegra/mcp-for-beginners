from mcp.server.fastmcp import FastMCP
##from fastmcp import FastMCP
import random

mcp = FastMCP("ServidorMCPHoroscopo")

@mcp.tool()
def obtener_horoscopo(sign: str) -> str:
    """
    Devuelve un horóscopo simple para un signo del zodiaco.
    """
    predictions = [
        "Hoy es un buen día para nuevas oportunidades.",
        "Mantén la calma, se acerca una buena noticia.",
        "Confía en tus instintos y sigue adelante.",
        "Podrías recibir ayuda inesperada de alguien cercano."
    ]
    return f"El horóscopo de hoy para {sign.capitalize()} dice que {random.choice(predictions)}"

if __name__ == "__main__":
    mcp.run()