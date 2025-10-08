import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';

// crear el servidor
const server = new McpServer({
    name: "srv-mcp-conversor-monedas",
    description: "Un servidor que convierte entre diferentes monedas utilizando tasas de cambio actualizadas.",
    version: "1.0.0",
});

// crear una herramienta para sacar el valor de la moneda
server.tool(
    "valor_monedas",
    "Obtiene el valor actual de una moneda en USD.",
    {
        currency: z.string().min(1).describe("Código de la moneda (EUR, USD, JPY, etc.)")
    },
    async ({ currency }) => {
        const url = "https://cdn.moneyconvert.net/api/latest.json";
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error("Error al obtener las tasas de cambio.");
        }

        const data = await response.json();
        const value = data.rates[currency.toUpperCase()];

        if (!value) {
            throw new Error("Moneda no soportada. Usa EUR, USD, JPY...");
        }

        return {
            content: [
                {
                    type: "text",
                    text: `El valor actual de ${currency.toUpperCase()} en USD es ${value}`
                }
            ]
        };
    }
);

// crear una herramienta para convertir entre monedas
server.tool(
    "conversion_monedas",
    "Convierte una cantidad de una moneda a otra utilizando tasas de cambio actualizadas.",
    {
        origin: z.string().length(3).describe("Código de la moneda origen (EUR, USD, JPY, etc.)"),
        destination: z.string().length(3).describe("Código de la moneda destino (EUR, USD, JPY, etc.)"),
        amount: z.number().describe("Cantidad a convertir")
    },
    async ({ origin, destination, amount }) => {
        const url = "https://cdn.moneyconvert.net/api/latest.json";
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error("Error al obtener las tasas de cambio.");
        }

        const data = await response.json();
        const rates = data.rates;

        if (!rates) {
            throw new Error("Error en los datos de las tasas de cambio.");
        }

        // La moneda base es USD (implícito en la API)
        const base = "USD";
        
        const originUpper = origin.toUpperCase();
        const destinationUpper = destination.toUpperCase();

        // Verificar que las monedas existen en las tasas
        if (originUpper !== base && !rates[originUpper]) {
            throw new Error(`Moneda origen no soportada: ${originUpper}`);
        }
        if (destinationUpper !== base && !rates[destinationUpper]) {
            throw new Error(`Moneda destino no soportada: ${destinationUpper}`);
        }

        let rate;

        // Si ambas son la misma moneda
        if (originUpper === destinationUpper) {
            rate = 1;
        }
        // Si origin es la moneda base (USD)
        else if (originUpper === base) {
            rate = rates[destinationUpper];
        }
        // Si destination es la moneda base (USD)
        else if (destinationUpper === base) {
            rate = 1 / rates[originUpper];
        }
        // Conversión entre dos monedas que no son base
        else {
            // Primero convertimos origin a base, luego base a destination
            rate = rates[destinationUpper] / rates[originUpper];
        }

        const convertedAmount = amount * rate;

        return {
            content: [
                {
                    type: "text",
                    text: `${amount} ${origin.toUpperCase()} = ${convertedAmount.toFixed(2)} ${destination.toUpperCase()}`
                }
            ]
        };
    }
);



// conectar el servidor a stdio.
const transport = new StdioServerTransport();
await server.connect(transport);