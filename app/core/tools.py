from typing import Protocol, Any, Dict, Optional

class Tool(Protocol):
    name: str
    description: str
    parameters: Dict[str, Any]
    async def __call__(self, **kwargs) -> Any: ...

class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def register(self, t: Tool):
        self._tools[t.name] = t

    def get(self, name: str) -> Tool | None:
        return self._tools.get(name)

    def as_openai_spec(self) -> list[dict]:
        out = []
        for t in self._tools.values():
            out.append({
                "type": "function",
                "function": {
                    "name": t.name,
                    "description": t.description,
                    "parameters": t.parameters,
                }
            })
        return out

