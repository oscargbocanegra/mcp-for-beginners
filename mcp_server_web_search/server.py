from __future__ import annotations

import os
import json
import httpx
import logging
from typing import Dict, Any
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP, Context

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
if not SERPAPI_KEY:
    logger.error("SERPAPI_KEY environment variable not found. Please configure your SerpApi key in .env file.")
    raise EnvironmentError("SERPAPI_KEY environment variable is required")

SERPAPI_BASE_URL = "https://serpapi.com/search"
DEFAULT_TIMEOUT = 10.0
DEFAULT_RESULTS_LIMIT = 5

mcp = FastMCP("WebSearchServer")

async def make_serpapi_request(ctx: Context, params: Dict[str, Any]) -> Dict[str, Any]:
    """Make a request to SerpApi with proper error handling."""
    request_params = {**params, "api_key": SERPAPI_KEY}
    
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            await ctx.info(f"Making SerpAPI request with engine: {params.get('engine', 'google')}")
            response = await client.get(SERPAPI_BASE_URL, params=request_params)
            response.raise_for_status()
            data = response.json()
            await ctx.info("Received response from SerpAPI")
            return data
    except httpx.TimeoutException:
        await ctx.error("Request to SerpApi timed out")
        raise Exception("Request to SerpApi timed out")
    except httpx.RequestError as e:
        await ctx.error(f"Request error to SerpApi: {e}")
        raise Exception(f"Request to SerpApi failed: {e}")
    except httpx.HTTPStatusError as e:
        await ctx.error(f"HTTP error from SerpApi: {e.response.status_code} - {e.response.text}")
        raise Exception(f"HTTP error from SerpApi: {e.response.status_code}")
    except json.JSONDecodeError:
        await ctx.error("Failed to decode JSON response from SerpApi")
        raise Exception("Failed to decode JSON response from SerpApi")

@mcp.tool()
async def general_search(query: str, num_results: int = DEFAULT_RESULTS_LIMIT, ctx: Context = None) -> str:
    """Perform a general web search using SerpApi."""
    await ctx.info(f"Performing general search for: {query} with {num_results} results")

    try:
        params = {
            "q": query,
            "num": num_results,
            "engine": "google"
        }

        response_data = await make_serpapi_request(ctx, params)
        organic_results = response_data.get("organic_results", [])
        
        if not organic_results:
            await ctx.info("No organic results found")
            return "No organic results found."
        
        formatted_results = []
        for i, result in enumerate(organic_results[:num_results]):
            formatted_results.append(
                f"## {i+1}. {result.get('title', 'No title')}\n"
                f"**Link**: {result.get('link', 'No link')}\n"
                f"**Snippet**: {result.get('snippet', 'No summary')}\n"
            )
        
        await ctx.info(f"Found {len(organic_results)} organic results")
        return "\n\n".join(formatted_results)
        
    except Exception as e:
        await ctx.error(f"Error performing general search: {str(e)}")
        return f"Error performing general search: {str(e)}"

@mcp.tool()
async def news_search(query: str, num_results: int = DEFAULT_RESULTS_LIMIT, ctx: Context = None) -> str:
    """Perform a news search using SerpApi."""
    await ctx.info(f"Performing news search for: {query} with {num_results} results")

    try:
        params = {
            "q": query,
            "num": num_results,
            "engine": "google_news"
        }

        response_data = await make_serpapi_request(ctx, params)
        news_results = response_data.get("news_results", [])
        
        if not news_results:
            await ctx.info("No news results found")
            return "No news results found."
        
        formatted_results = []
        for i, result in enumerate(news_results[:num_results]):
            formatted_results.append(
                f"## {i+1}. {result.get('title', 'No title')}\n"
                f"**Source**: {result.get('source', 'No source')}\n"
                f"**Date**: {result.get('date', 'No date')}\n"
                f"**Link**: {result.get('link', 'No link')}\n"
                f"**Snippet**: {result.get('snippet', 'No summary')}\n"
            )
        
        await ctx.info(f"Found {len(news_results)} news results")
        return "\n\n".join(formatted_results)
        
    except Exception as e:
        await ctx.error(f"Error performing news search: {str(e)}")
        return f"Error performing news search: {str(e)}"

@mcp.tool()
async def product_search(query: str, num_results: int = DEFAULT_RESULTS_LIMIT, ctx: Context = None) -> str:
    """Perform a product search using SerpApi."""
    await ctx.info(f"Performing product search for: {query} with {num_results} results")

    try:
        params = {
            "q": query,
            "num": num_results,
            "engine": "google_shopping",
            "shopping_intent": "high"
        }

        response_data = await make_serpapi_request(ctx, params)
        product_results = response_data.get("shopping_results", [])
        
        if not product_results:
            await ctx.info("No product results found")
            return "No product results found."
        
        formatted_results = []
        for i, result in enumerate(product_results[:num_results]):
            formatted_results.append(
                f"## {i+1}. {result.get('title', 'No title')}\n"
                f"**Price**: {result.get('price', 'No price')}\n"
                f"**Rating**: {result.get('rating', 'No rating')}\n"
                f"({result.get('reviews', 'No reviews')})\n"
                f"**Source**: {result.get('source', 'No source')}\n"
                f"**Link**: {result.get('link', 'No link')}\n"
            )
        
        await ctx.info(f"Found {len(product_results)} product results")
        return "\n\n".join(formatted_results)
        
    except Exception as e:
        await ctx.error(f"Error performing product search: {str(e)}")
        return f"Error performing product search: {str(e)}"

@mcp.tool()
async def qna(question: str, ctx: Context = None) -> str:
    """Perform a question and answer search using SerpApi."""
    await ctx.info(f"Performing Q&A search for: {question}")

    try:
        params = {
            "q": question,
            "engine": "google",
        }

        response_data = await make_serpapi_request(ctx, params)

        # Check for direct answer
        answer_results = response_data.get("answer_box", {})
        if answer_results:
            await ctx.info("Found direct answer")
            if "answer" in answer_results:
                return f"**Answer**: {answer_results['answer']}\n\n"
            elif "snippet" in answer_results:
                return f"**Answer**: {answer_results['snippet']}\n\n"
            elif "snippet_highlighted_words" in answer_results:
                return f"**Answer**: {' '.join(answer_results['snippet_highlighted_words'])}\n\n"
        
        # Check knowledge graph
        knowledge_results = response_data.get("knowledge_graph", {})
        if knowledge_results and "description" in knowledge_results:
            await ctx.info("Found knowledge graph information")
            return f"**Description**: {knowledge_results['description']}\n\n"
        
        # Check featured snippet
        if "featured_snippet" in response_data:
            featured_snippet = response_data["featured_snippet"]
            if "text" in featured_snippet:
                await ctx.info("Found featured snippet")
                return f"**Featured Snippet**: {featured_snippet['text']}\n\n"
        
        # Related questions
        related_questions = response_data.get("related_questions", [])
        if related_questions:
            await ctx.info("Found related questions")
            formatted_questions = []
            for i, question in enumerate(related_questions):
                formatted_questions.append(
                    f"## {i+1}. {question.get('question', 'No question')}\n"
                    f"**Link**: {question.get('link', 'No link')}\n"
                )
            return "\n\n".join(formatted_questions)
        
        # Fallback to organic results
        organic_results = response_data.get("organic_results", [])
        if organic_results:
            await ctx.info("Found organic results")
            formatted_results = []
            for i, result in enumerate(organic_results[:5]):
                formatted_results.append(
                    f"## {i+1}. {result.get('title', 'No title')}\n"
                    f"**Link**: {result.get('link', 'No link')}\n"
                    f"**Snippet**: {result.get('snippet', 'No summary')}\n"
                )
            return "\n\n".join(formatted_results)
            
        return "No results found for the question."
        
    except Exception as e:
        await ctx.error(f"Error performing Q&A search: {str(e)}")
        return f"Error performing Q&A search: {str(e)}"

if __name__ == "__main__":
    mcp.run()