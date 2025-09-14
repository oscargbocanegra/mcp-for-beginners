import aiohttp
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Servidor de enrutamiento con herramientas")

class McpToolRouter:
    def __init__(self):
        self.tool_endpoints = {
            "weatherTool": "https://weather-service.example.com/api",
            "calculatorTool": "https://calculator-service.example.com/compute",
            "databaseTool": "https://database-service.example.com/query",
            "searchTool": "https://search-service.example.com/search",
        }
    
    async def route_tool_requests(self, tool_name, parameters):
        """Enruta una solicitud de herramienta a su servicio correspondiente."""
        endpoint = self.tool_endpoints.get(tool_name)
        if not endpoint:
            raise ValueError(f"No hay un endpoint disponible para la herramienta: {tool_name}")
        
        return await self.execute_tool_request(endpoint, tool_name, parameters)

    async def execute_tool_request(self, endpoint, tool_name, parameters):
        """Ejecuta la solicitud a la herramienta en el endpoint especificado."""
        async with aiohttp.ClientSession() as session:
            async with session.post(endpoint, json={"toolName": tool_name, "parameters": parameters}) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Error al llamar a la herramienta {tool_name}: {response.status} - {await response.text()}")
                
mcp_tool_router = McpToolRouter()

@mcp.tool()
async def execute_tool(tool_name: str, parameters: dict) -> dict:
    """Ejecuta una herramienta específica con los parámetros dados."""
    return await mcp_tool_router.route_tool_requests(tool_name, parameters)

if __name__ == "__main__":
    mcp.run()
