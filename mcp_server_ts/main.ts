import { McpServer, ResourceTemplate } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';

const server = new McpServer({
    name: "server-mcp-ts",
    version: "0.0.1"
});

server.registerTool("multiplicar",
    {
        title: "Multiplicar",
        description: "Multiplica dos números",
        inputSchema: { number1: z.number(), number2: z.number() }
    },

    async ({ number1, number2 }) => {

        if (typeof number1 !== "number" || typeof number2 !== "number") {
            throw new Error("Los parámetros deben ser números");
        }
        return {
            content: [
                {
                    type: "text",
                    text: String(number1 * number2)
                }
            ]
        };
    }
);

server.registerResource(
    "saludar",
    new ResourceTemplate("saludar://{nombre}", { list: undefined }),
    { title: "Saludar", description: "Saluda a una persona por su nombre" },
    async (url, { nombre }) => {
        if (typeof nombre !== "string") {
            throw new Error("El parámetro nombre debe ser una cadena de texto");
        }
        return {
            contents: [
                {
                    uri: url.href,
                    text: `Hola, ${nombre}!`
                }
            ]
        }
    }
);

//conexion del server con la IA
const transport = new StdioServerTransport();
await server.connect(transport);

//conexion del server con HTTP
//const httpTransport = new StreamableHTTPServerTransport({port: 8080});
//await server.connect(httpTransport);
