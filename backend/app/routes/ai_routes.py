from fastapi import APIRouter
from ..controllers import ai_controller

router = APIRouter()
router.include_router(ai_controller.router)
