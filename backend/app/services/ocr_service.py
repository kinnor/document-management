from __future__ import annotations

"""OCR extraction service using Tesseract and pdf2image."""

from typing import List
import logging
import os

from pdf2image import convert_from_path
import pytesseract


logger = logging.getLogger(__name__)


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF file.

    This converts each PDF page to an image using ``pdf2image`` and runs
    Tesseract OCR on the result.

    Parameters
    ----------
    pdf_path:
        Path to the PDF document.

    Returns
    -------
    str
        The text recognized from all pages.

    Raises
    ------
    FileNotFoundError
        If ``pdf_path`` does not point to an existing file.
    RuntimeError
        If conversion or OCR fails.
    """
    if not os.path.isfile(pdf_path):
        logger.error("PDF file does not exist: %s", pdf_path)
        raise FileNotFoundError(f"{pdf_path} does not exist")

    try:
        # Use a moderate DPI to balance quality and performance
        logger.info("Converting PDF to images: %s", pdf_path)
        images = convert_from_path(pdf_path, dpi=200)
    except Exception as exc:  # pragma: no cover - external tool failure
        logger.error("Failed converting PDF to images: %s", exc)
        raise RuntimeError(f"Failed converting PDF to images: {exc}") from exc

    texts: List[str] = []
    for img in images:
        try:
            logger.debug("Running OCR on image")
            texts.append(pytesseract.image_to_string(img))
        except Exception as exc:  # pragma: no cover - external tool failure
            logger.error("Tesseract OCR failed: %s", exc)
            raise RuntimeError(f"Tesseract OCR failed: {exc}") from exc
        finally:
            img.close()

    result = "\n".join(texts)
    logger.info("OCR extraction completed for %s", pdf_path)
    return result
