from mcp.server.fastmcp import FastMCP
import random

mcp = FastMCP("ServidorMCPHoroscopo")

@mcp.tool()
def obtener_horoscopo(signo: str) -> str:
    horoscopos = {
        "aries": "Hoy es un buen día para tomar decisiones importantes.",
        "tauro": "La paciencia será tu mejor aliada hoy.",
        "géminis": "La comunicación será clave en tus relaciones.",
        "cáncer": "Confía en tus instintos y sigue tu corazón.",
        "leo": "Tu creatividad estará en su punto máximo.",
        "virgo": "Organiza tus ideas para alcanzar tus metas.",
        "libra": "Busca el equilibrio en todas las áreas de tu vida.",
        "escorpio": "La pasión te guiará hacia nuevas oportunidades.",
        "sagitario": "Aventúrate fuera de tu zona de confort.",
        "capricornio": "El trabajo duro dará frutos pronto.",
        "acuario": "Innova y piensa fuera de lo común.",
        "piscis": "Deja que tu intuición te lleve a lugares inesperados."
    }
    signo = signo.lower()
    return horoscopos.get(signo, random.choice(list(horoscopos.values())))

if __name__ == "__main__":
    mcp.run()