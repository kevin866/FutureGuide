class EchoTool:
    name = "echo"
    description = "Echo back the provided text"
    parameters = {"type":"object","properties":{"text":{"type":"string"}},"required":["text"]}

    async def __call__(self, text: str):
        return {"echo": text}
