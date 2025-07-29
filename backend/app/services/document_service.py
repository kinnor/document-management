from typing import List
import logging

from ..models.document_model import Document


logger = logging.getLogger(__name__)

class DocumentService:
    def __init__(self):
        self._documents: List[Document] = []

    def list_documents(self) -> List[Document]:
        logger.info("Listing %d documents", len(self._documents))
        return self._documents

    def create_document(self, document: Document) -> Document:
        if any(doc.id == document.id for doc in self._documents):
            logger.error("Document with id %s already exists", document.id)
            raise ValueError(f"Document with id {document.id} already exists")

        self._documents.append(document)
        logger.info("Document created: %s", document.id)
        return document

document_service = DocumentService()
