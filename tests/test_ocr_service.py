import os
from unittest import mock
import pytest

from backend.app.services.ocr_service import extract_text_from_pdf


def test_extract_text_from_pdf(monkeypatch, tmp_path):
    pdf = tmp_path / "sample.pdf"
    pdf.write_bytes(b"data")
    fake_img = mock.MagicMock()

    monkeypatch.setattr(
        "backend.app.services.ocr_service.convert_from_path",
        lambda path, dpi=200: [fake_img],
    )
    monkeypatch.setattr(
        "backend.app.services.ocr_service.pytesseract.image_to_string",
        lambda img: "text",
    )

    assert extract_text_from_pdf(str(pdf)) == "text"
    fake_img.close.assert_called()


def test_extract_text_missing_file():
    with pytest.raises(FileNotFoundError):
        extract_text_from_pdf("missing.pdf")
