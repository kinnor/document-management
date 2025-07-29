from __future__ import annotations

"""OCR endpoints."""

import os
import shutil
import tempfile

import logging
from fastapi import APIRouter, File, HTTPException, UploadFile

from ..models.ocr_model import OCRResult

from ..services.ocr_service import extract_text_from_pdf


logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/extract", response_model=OCRResult)
async def extract_text(file: UploadFile = File(...)) -> OCRResult:
    """Extract text from an uploaded PDF file using OCR."""
    logger.info("POST /ocr/extract")
    if file.content_type != "application/pdf":
        logger.error("Unsupported file type: %s", file.content_type)
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    tmp_path = ""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        text = extract_text_from_pdf(tmp_path)
    except FileNotFoundError as exc:
        logger.error("File not found during OCR: %s", exc)
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except Exception as exc:  # pragma: no cover - external tool failure
        logger.error("Unexpected OCR error: %s", exc)
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    finally:
        file.file.close()
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)
            logger.debug("Temporary file removed: %s", tmp_path)

    logger.info("OCR extraction successful")
    return OCRResult(text=text)
