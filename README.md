# llm-agents-from-scratch

# 01 — CLI Research Agent

A terminal-based AI agent that searches the web to answer your questions. Built with raw OpenAI SDK — no LangChain, no LangGraph.

## What it does

- Takes your question in the terminal
- Decides whether it needs to search the web or can answer directly
- If it needs to search, calls DuckDuckGo, gets results, reasons over them
- Returns a final answer

## How it works

This is a manual implementation of the ReAct loop (Reason → Act → Observe):

```
User asks question
    → LLM decides: search or answer directly?
    → If search: calls web_search tool
    → Gets results back, reasons over them
    → Returns final answer
```

## Stack

- Python 3.14
- OpenAI SDK — LLM calls and tool calling
- ddgs — DuckDuckGo search, no API key needed
- python-dotenv — loads API key from .env

## Project Structure

```
01_cli_research_agent/
├── main.py          # Entry point, starts the loop
├── agent.py         # ReAct loop logic
├── tools.py         # web_search function
└── tool_schemas.py  # Tool description passed to OpenAI
```

## Setup

1. Clone the repo
```bash
git clone https://github.com/mahifriends555/llm-agents-from-scratch.git
cd llm-agents-from-scratch/projects/01_cli_research_agent
```

2. Create and activate virtual environment
```bash
python -m venv Agent1

# Windows (PowerShell)
Agent1\Scripts\activate

# Windows (Git Bash)
source Agent1/Scripts/activate

# Mac/Linux
source Agent1/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Add your OpenAI API key
```bash
# Create a .env file and add:
OPENAI_API_KEY=your_key_here
```

5. Run
```bash
python main.py
```

## Example

```
You: Who won IPL 2025?
Calling tool: web_search with {'query': 'IPL 2025 winner'}

Agent: The IPL 2025 was won by...

You: What is 2+2?

Agent: 2+2 is 4.
```