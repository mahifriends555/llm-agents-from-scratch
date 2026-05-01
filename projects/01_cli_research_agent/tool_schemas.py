

tools = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Use this to search the web for current or recent information that you don't already know",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query, like 'IPL 2025 winner' or 'current gold price India'"
                    }
                },
                "required": ["query"]
            }
        }
    }
]
