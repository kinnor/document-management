from __future__ import annotations

"""OCR endpoints."""

import os
import shutil
import tempfile

from fastapi import APIRouter, File, HTTPException, UploadFile

from ..services.ocr_service import extract_text_from_pdf

router = APIRouter()


@router.post("/extract")
async def extract_text(file: UploadFile = File(...)) -> dict[str, str]:
    """Extract text from an uploaded PDF file using OCR."""
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    tmp_path = ""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        text = extract_text_from_pdf(tmp_path)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except Exception as exc:  # pragma: no cover - external tool failure
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    finally:
        file.file.close()
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)

    return {"text": text}
