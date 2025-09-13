from fastapi import FastAPI, UploadFile, File
from mcp.server.fastmcp import FastMCP
from PIL import Image

import numpy as np

app = FastAPI()
mcp = FastMCP("MultimodalServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting."""
    return f"Hello, {name}!"

@app.post("/image/brightness")
async def analyze_brightness(file: UploadFile = File(...)):
    """Analyze the brightness of an uploaded image."""
    image = Image.open(file.file).convert("L")
    np_image = np.array(image)
    brightness = np.mean(np_image)
    return {"brightness": brightness, "message": "Image brightness analyzed successfully."}

app.mount("/mcp", mcp)


# ¿Cómo ejecutar y probar tu servidor?
# Para ejecutar tu servidor, utiliza Uvicorn desde la terminal:
# uv run uvicorn mcp_server_images.server:app --reload --host 0.0.0.0 --port 8000

# Confirma tu servidor enviando una imagen mediante una petición CURL de esta forma:
#    curl -X POST http://localhost:8000/image/brightness -F "file=@jardin.jpg"