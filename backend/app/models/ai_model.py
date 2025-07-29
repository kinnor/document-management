from pydantic import BaseModel


class AIRequest(BaseModel):
    text: str


class AIResponse(BaseModel):
    result: str
