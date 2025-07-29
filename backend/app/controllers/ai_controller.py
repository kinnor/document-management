import logging
from fastapi import APIRouter, HTTPException

from ..models.ai_model import AIRequest, AIResponse
from ..services.ai_service import generate_summary


logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/generate", response_model=AIResponse)
def generate(request: AIRequest) -> AIResponse:
    logger.info("POST /ai/generate")
    try:
        result = generate_summary(request.text)
    except Exception as exc:
        logger.error("AI generation failed: %s", exc)
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    logger.info("AI generation successful")
    return AIResponse(result=result)
