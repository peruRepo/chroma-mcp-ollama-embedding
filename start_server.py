#!/usr/bin/env python3
"""
Test script to verify the Chroma MCP server can start properly
"""
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from chroma_mcp.server import main

if __name__ == "__main__":
    main()
