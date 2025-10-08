import { McpServer, ResourceTemplate } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';

//creacion del server
const server = new McpServer({
    name: "server-mcp-calculadora-ts",
    version: "0.0.1"
});

//registro de herramientas y recursos
server.registerTool("sumar",
    {
        title: "Sumar",
        description: "Suma dos números",
        inputSchema: { n1: z.number(), n2: z.number() }
    },

    async ({ n1, n2 }) => {
        let operation: string = String(n1 + n2);

        return {
            content: [ {   type: "text", text: operation } ]
        };
    }
);

server.registerTool("restar",
    {
        title: "Restar",
        description: "Resta dos números",
        inputSchema: { n1: z.number(), n2: z.number() }
    },

    async ({ n1, n2 }) => {
        let operation: string = String(n1 - n2);

        return {
            content: [ {   type: "text", text: operation } ]
        };
    }
);

server.registerTool("multiplicar",
    {
        title: "Multiplicar",
        description: "Multiplicar dos números",
        inputSchema: { n1: z.number(), n2: z.number() }
    },

    async ({ n1, n2 }) => {
        let operation: string = String(n1 * n2);

        return {
            content: [ {   type: "text", text: operation } ]
        };
    }
);

server.registerTool("dividir",
    {
        title: "Dividir",
        description: "Dividir dos números",
        inputSchema: { n1: z.number(), n2: z.number() }
    },

    async ({ n1, n2 }) => {
        let operation: string = String(n1 % n2);

        return {
            content: [ {   type: "text", text: operation } ]
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
