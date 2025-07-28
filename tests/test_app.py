from fastapi.testclient import TestClient
from backend.app.main import app

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
