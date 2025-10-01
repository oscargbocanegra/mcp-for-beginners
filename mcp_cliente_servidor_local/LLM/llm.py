import os
import json
from openai import OpenAI

# Reemplaza o usa variable de entorno
OPEN_API_KEY = "OPEN_API_KEY"

client = OpenAI(api_key=OPEN_API_KEY)

def build_prompt(user_message: str) -> str:
    return f"""
Eres un asistente que recibe instrucciones en lenguaje natural y decide qué herramienta MCP invocar.

Herramientas disponibles:

1. obtener_horoscopo(sign: string) - Devuelve el horoscopo para un signo del zodiaco.

Responde solo con JSON como este:

{{
  "tool": "obtener_horoscopo",
  "arguments": {{
    "sign": "Libra"
  }}
}}

Usuario: {user_message}
"""

async def interpret_with_gpt(user_message: str):
    prompt = build_prompt(user_message)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw = response.choices[0].message.content
    return json.loads(raw)
