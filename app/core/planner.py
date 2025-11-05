import json
from .llm import OpenAIProvider
from .tools import ToolRegistry

SYSTEM_PROMPT = (
    "You are a backend AI agent. Prefer using tools when available. "
    "Be concise. If insufficient context, state assumptions."
)

async def run_turn(llm: OpenAIProvider, registry: ToolRegistry, user_text: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_text},
    ]
    resp = await llm.chat(messages, tools=registry.as_openai_spec())
    msg = resp["choices"][0]["message"]

    if "tool_calls" in msg:
        tool_msgs = []
        for call in msg["tool_calls"]:
            name = call["function"]["name"]
            args_json = call["function"].get("arguments", "{}")
            args = json.loads(args_json) if args_json else {}
            tool = registry.get(name)
            payload = await tool(**args) if tool else {"error": f"Tool {name} not found"}
            tool_msgs.append({
                "role": "tool",
                "tool_call_id": call["id"],
                "name": name,
                "content": json.dumps(payload)
            })
        messages.extend([msg, *tool_msgs])
        follow = await llm.chat(messages, tools=None)
        return follow["choices"][0]["message"]["content"]

    return msg.get("content", "")
