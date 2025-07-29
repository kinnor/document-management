from fastapi.testclient import TestClient
from backend.app.main import app
from unittest import mock

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Document Management API"}


def test_create_and_list_documents():
    doc = {"id": 1, "title": "Doc 1", "content": "Content"}
    post_resp = client.post("/documents/", json=doc)
    assert post_resp.status_code == 200
    assert post_resp.json() == doc

    list_resp = client.get("/documents/")
    assert list_resp.status_code == 200
    assert list_resp.json() == [doc]


def test_ocr_endpoint(monkeypatch, tmp_path):
    sample_pdf = tmp_path / "sample.pdf"
    sample_pdf.write_bytes(b"dummy")

    def fake_extract(path):
        assert path == str(sample_pdf)
        return "ocr text"

    monkeypatch.setattr(
        "backend.app.services.ocr_service.extract_text_from_pdf", fake_extract
    )

    with sample_pdf.open("rb") as f:
        resp = client.post(
            "/ocr/extract",
            files={"file": ("sample.pdf", f, "application/pdf")},
        )

    assert resp.status_code == 200
    assert resp.json() == {"text": "ocr text"}
