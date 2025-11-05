from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class ChatIn(BaseModel):
    message: str = Field(..., min_length=1)

class ChatOut(BaseModel):
    reply: str

class IngestChunk(BaseModel):
    content: str
    source: Optional[str] = None
    kind: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None

class IngestIn(BaseModel):
    chunks: List[IngestChunk]
