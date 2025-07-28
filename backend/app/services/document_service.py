from typing import List
from ..models.document_model import Document

class DocumentService:
    def __init__(self):
        self._documents: List[Document] = []

    def list_documents(self) -> List[Document]:
        return self._documents

    def create_document(self, document: Document) -> Document:
        self._documents.append(document)
        return document

document_service = DocumentService()
