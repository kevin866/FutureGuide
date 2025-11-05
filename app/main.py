from fastapi import FastAPI
from .schemas.chat import ChatIn, ChatOut
from .core.config import settings
from .core.llm import OpenAIProvider
from .core.tools import ToolRegistry
from .core.planner import run_turn

# 注册内置工具
from .tools.datetime_tool import DateTimeTool
from .tools.calculator_tool import CalculatorTool
from .tools.echo_tool import EchoTool
# 可选
# from .tools.file_loader_tool import FileLoaderTool

app = FastAPI(title="AI Agent Backend")

llm = OpenAIProvider()
registry = ToolRegistry()
for t in (DateTimeTool(), CalculatorTool(), EchoTool()):
    registry.register(t)
# 可选
# registry.register(FileLoaderTool())

@app.post("/chat", response_model=ChatOut)
async def chat(payload: ChatIn):
    reply = await run_turn(llm, registry, payload.message)
    return {"reply": reply}

@app.get("/healthz")
async def healthz():
    return {"ok": True}
