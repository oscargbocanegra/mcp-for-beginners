import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
    name: "srv-mcp-weather",
    description: "Un servidor que proporciona información meteorológica actualizada para diferentes ciudades del mundo.",
    version: "1.0.0",
});

// crear una herramienta para obtener el clima actual de una ciudad
server.registerTool("clima_actual",
    {
        title: "Obtiene el clima actual de una ciudad.",
        description: "Proporciona información meteorológica actualizada para una ciudad específica.",
        inputSchema: { 
            city: z.string().min(2).describe("Nombre de la ciudad (por ejemplo, 'Madrid', 'New York', 'Tokyo')")
        }
    },
    async ({ city }) => {
        try {
            const geoUrl = `https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(city)}&count=1`;
            const geoResponse = await fetch(geoUrl);
            
            if (!geoResponse.ok) {
                throw new Error("Error al obtener las coordenadas de la ciudad.");
            }

            const geoData = await geoResponse.json();
            
            if (!geoData.results || geoData.results.length === 0) {
                throw new Error(`Ciudad '${city}' no encontrada. Intenta con otro nombre.`);
            }

            const { latitude, longitude, name, country } = geoData.results[0];
            const weatherUrl = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current=temperature_2m,precipitation,wind_speed_10m,weather_code&timezone=auto`;
            const weatherResponse = await fetch(weatherUrl);
            
            if (!weatherResponse.ok) {
                throw new Error("Error al obtener los datos meteorológicos.");
            }

            const weatherData = await weatherResponse.json();

            return {
                content: [
                    {
                        type: "text",
                        text: JSON.stringify({
                            ciudad: name,
                            pais: country,
                            coordenadas: { latitude, longitude },
                            clima_actual: weatherData.current,
                            unidades: weatherData.current_units,
                            datos_completos: weatherData
                        }, null, 2)
                    }
                ]
            };
        } catch (error) {
            return {
                content: [
                    {
                        type: "text",
                        text: `Error: ${error.message}`
                    }
                ],
                isError: true
            };
        }
    }
)




const transport = new StdioServerTransport();
await server.connect(transport);