import asyncio
import json
import pathlib
import sys
from pathlib import Path 

import ollama 
from mcp import ClientSession,StdioServerParameters 
from mcp.client.stdion import stdio_client