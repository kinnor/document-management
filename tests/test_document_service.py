"""Unit tests for the DocumentService."""

import pytest

from backend.app.models.document_model import Document
from backend.app.services.document_service import DocumentService


@pytest.fixture()
def service():
    """Return a fresh DocumentService for each test."""
    return DocumentService()


def test_create_and_list_documents(service):
    """Documents can be created and then listed."""
    doc = Document(id=1, title="Doc", content="text")
    created = service.create_document(doc)
    assert created == doc
    assert service.list_documents() == [doc]


def test_create_document_duplicate(service):
    """Creating a document with an existing id raises ValueError."""
    doc = Document(id=1, title="Doc")
    service.create_document(doc)
    with pytest.raises(ValueError):
        service.create_document(doc)
