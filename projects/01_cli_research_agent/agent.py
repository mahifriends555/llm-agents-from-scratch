
from dotenv import load_dotenv
load_dotenv()

import json
from openai import OpenAI
from tools import web_search
from tool_schemas import tools

client = OpenAI()

TOOL_MAP = {
    "web_search": web_search
}

def run_agent(user_question: str):
    messages = [
        {"role": "system", "content": "You are a helpful research assistant. Use the web_search tool when you need current or recent information."},
        {"role": "user", "content": user_question}
    ]

    while True:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools
        )

        message = response.choices[0].message

        # Model gave a direct answer
        if message.tool_calls is None:
            print("\nAgent:", message.content)
            break

        # Model wants to use a tool
        messages.append(message)

        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print(f"\nCalling tool: {function_name} with {arguments}")

            result = TOOL_MAP[function_name](**arguments)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })
