from fastapi import APIRouter
from ..controllers import document_controller

router = APIRouter()

router.include_router(document_controller.router)
