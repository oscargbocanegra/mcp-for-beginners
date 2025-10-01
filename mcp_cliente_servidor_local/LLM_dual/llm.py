import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Reemplaza o usa variable de entorno
load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=OPEN_API_KEY)

def build_prompt(user_message: str) -> str:
    return f"""
Eres un asistente que puede:
1️⃣ Usar una herramienta para obtener horóscopos si el usuario lo pide.
2️⃣ Responder normalmente (texto libre) si la pregunta no es de horóscopo.

Herramienta disponible:
- obtener_horoscopo(sign: string) → Devuelve el horóscopo para un signo del zodiaco.

Ejemplos:

Usuario: "Dame el horóscopo de Aries"
Respuesta:
{{
  "tool": "obtener_horoscopo",
  "arguments": {{
    "sign": "Aries"
  }}
}}

Usuario: "Hola, ¿cómo estás?"
Respuesta:
{{
  "response": "¡Hola! Estoy aquí para ayudarte. ¿En qué puedo asistirte hoy?"
}}

Usuario: "¿Quién fue Albert Einstein?"
Respuesta:
{{
  "response": "Albert Einstein fue un físico alemán conocido por la teoría de la relatividad."
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

    try:
        return json.loads(raw)
    except Exception:
        return {"response": raw}
 
