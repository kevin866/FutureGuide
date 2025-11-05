import httpx
from .config import settings

class OpenAIProvider:
    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY
        self.base = "https://api.openai.com/v1"
        self.chat_model = settings.OPENAI_CHAT_MODEL
        self.embed_model = settings.OPENAI_EMBED_MODEL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def chat(self, messages: list[dict], tools: list[dict] | None = None) -> dict:
        payload = {"model": self.chat_model, "messages": messages, "temperature": 0.2}
        if tools:
            payload["tools"] = tools
            payload["tool_choice"] = "auto"
        async with httpx.AsyncClient(timeout=120) as client:
            r = await client.post(f"{self.base}/chat/completions", headers=self.headers, json=payload)
            r.raise_for_status()
            return r.json()

    async def embed(self, texts: list[str]) -> list[list[float]]:
        payload = {"model": self.embed_model, "input": texts}
        async with httpx.AsyncClient(timeout=60) as client:
            r = await client.post(f"{self.base}/embeddings", headers=self.headers, json=payload)
            r.raise_for_status()
            data = r.json()["data"]
            return [d["embedding"] for d in data]
