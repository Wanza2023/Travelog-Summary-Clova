from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
    title: Optional[str] = None
    content: str

class Summary(BaseModel):
    summary: str