import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const server = new McpServer({
    name: "test",
    version: "1.0.0",
});

const schema = z.object({
    city: z.string()
});

server.tool("test", zodToJsonSchema(schema), async (args) => {
    console.error("Args received:", JSON.stringify(args));
    return {
        content: [{ type: "text", text: `City: ${args.city}` }]
    };
});

const transport = new StdioServerTransport();
await server.connect(transport);
