from typing import List
from fastapi import APIRouter
from ..models.document_model import Document
from ..services.document_service import document_service

router = APIRouter()

@router.get("/", response_model=List[Document])
def get_documents():
    return document_service.list_documents()

@router.post("/", response_model=Document)
def create_document(document: Document):
    return document_service.create_document(document)
