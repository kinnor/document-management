from fastapi import APIRouter, HTTPException

from ..models.ai_model import AIRequest, AIResponse
from ..services.ai_service import generate_summary

router = APIRouter()


@router.post("/generate", response_model=AIResponse)
def generate(request: AIRequest) -> AIResponse:
    try:
        result = generate_summary(request.text)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return AIResponse(result=result)
