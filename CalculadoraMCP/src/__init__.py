import os
import sys
import time
from server import server

if __name__ == "__main__":
    """Main entry point"""
    transport_type = sys.argv[1] if len(sys.argv) > 1 else None
    server.settings.log_level = os.environ.get("LOG_LEVEL", "INFO")
    
    print(f"Starting Calculator MCP Server with transport: {transport_type}")
    
    if transport_type == "sse":
        port = int(os.environ.get("PORT", 3001))
        server.settings.port = port
        server.settings.host = "127.0.0.1"
        print(f"Server will run on http://{server.settings.host}:{port}")
        
        # Small delay to ensure proper initialization
        time.sleep(0.5)
        
        server.run(transport="sse")
    elif transport_type == "stdio":
        server.run(transport="stdio")
    else:
        print("Invalid transport type. Use 'sse' or 'stdio'.")
        sys.exit(1)