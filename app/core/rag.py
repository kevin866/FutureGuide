from .llm import OpenAIProvider

async def embed_texts(llm: OpenAIProvider, texts: list[str]) -> list[list[float]]:
    return await llm.embed(texts)
