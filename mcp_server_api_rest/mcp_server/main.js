import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import fs from "fs";
import FormData from "form-data";

const server = new McpServer({
    name: "mcp_server_api_rest",
    version: "1.0.0",
});

const BASE_URL = "http://localhost:3977/api/project";

server.registerTool("guardar_proyecto", {
    title: "Guardar Proyecto",
    description: "Guarda un proyecto en la base de datos",
    inputSchema: {
        name: z.string(),
        description: z.string(),
        category: z.string(),
        year: z.number().int(),
        state: z.string()
    }
}, async ({ name, description, category, year, state }) => {
    const response = await fetch(`${BASE_URL}/save`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, description, category, year, state })
    });
    if (!response.ok) throw new Error(`Error al guardar el proyecto`);
    const data = await response.json();
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
});

server.registerTool("listar_proyectos", {
    title: "Listar Proyectos",
    description: "Lista todos los proyectos en la base de datos"
}, async () => {
    const response = await fetch(`${BASE_URL}/list`);
    if (!response.ok) throw new Error(`Error al listar los proyectos`);
    const data = await response.json();
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
});


server.registerTool("obtener_proyecto", {
    title: "Obtener Proyecto",
    description: "Obtiene un proyecto por su ID",
    inputSchema: { id: z.string() }
}, async ({ id }) => {
    const response = await fetch(`${BASE_URL}/item/${id}`);
    if (!response.ok) throw new Error(`Error al obtener el proyecto con ID ${id}`);
    const data = await response.json();
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
});


server.registerTool("eliminar_proyecto", {
    title: "Eliminar Proyecto",
    description: "Elimina un proyecto por su ID",
    inputSchema: { id: z.string() }
}, async ({ id }) => {
    const response = await fetch(`${BASE_URL}/delete/${id}`, { method: "DELETE" });
    if (!response.ok) throw new Error(`Error al eliminar el proyecto con ID ${id}`);
    const data = await response.json();
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
});

server.registerTool("actualizar_proyectos", {
    title: "Actualizar Proyecto",
    description: "Actualiza un proyecto por su ID",
    inputSchema: {
        id: z.string(),
        name: z.string().optional(),
        description: z.string().optional(),
        category: z.string().optional(),
        year: z.number().int().optional(),
        state: z.string().optional()
    }
}, async ({ id, name, description, category, year, state }) => {
    const response = await fetch(`${BASE_URL}/update/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, description, category, year, state })
    });
    if (!response.ok) throw new Error(`Error al actualizar el proyecto con ID ${id}`);
    const data = await response.json();
    return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
});


server.registerTool("obtener_imagen_proyecto", {
    title: "Obtener Imagen Proyecto",
    description: "Obtiene la imagen de un proyecto por su ID",
    inputSchema: { file: z.string() }
}, async ({ file }) => {
    const response = await fetch(`${BASE_URL}/image/${file}`);
    if (!response.ok) throw new Error(`Error al obtener la imagen ${file}`);
    const blob = await response.arrayBuffer();
    const base64 = Buffer.from(blob).toString('base64');
    return {
        content: [{
            type: "text",
            data: base64,
            mimeType: response.headers.get("Content-Type")
        }]
    };
});


const transport = new StdioServerTransport();
await server.connect(transport);