from __future__ import annotations

"""Routes for OCR operations."""

from fastapi import APIRouter
from ..controllers import ocr_controller

router = APIRouter()
router.include_router(ocr_controller.router)
