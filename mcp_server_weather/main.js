import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
    name: "srv-mcp-weather",
    description: "Un servidor que proporciona información meteorológica actualizada para diferentes ciudades del mundo.",
    version: "1.0.0",
});


// crear una herramienta para obtener el clima actual de una ciudad
server.tool("clima_actual",
    {
        title: "Obtiene el clima actual de una ciudad.",
        description: "Proporciona información meteorológica actualizada para una ciudad específica.",
        city: z.string().min(2).describe("Nombre de la ciudad")
        
        /*
        inputSchema: {
            city: z.string().min(2, "Nombre de la ciudad")
        }
            */
    },

    async ({ city }) => {

        const geoUrl = `https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(city)}&count=1`;
        const geoResponse = await fetch(geoUrl);
        
        if (!geoResponse.ok) throw new Error("Error al obtener las coordenadas de la ciudad.");

        const geoData = await geoResponse.json();
        
        if (!geoData.results || geoData.results.length === 0) throw new Error("Ciudad no encontrada.");

        let { latitude, longitude } = geoData.results[0];
        const weatherUrl = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,precipitation&current=temperature_2m,precipitation`;
        const weatherResponse = await fetch(weatherUrl);
        
        if (!weatherResponse.ok) throw new Error("Error al obtener los datos meteorológicos.");

        const weatherData = await weatherResponse.json();

        return {
            content: [
                {
                    type: "text",
                    text: JSON.stringify(weatherData, null, 2)
                }
            ]
        }
    }
)




const transport = new StdioServerTransport();
await server.connect(transport);