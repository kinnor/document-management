from typing import List
import logging
from fastapi import APIRouter, HTTPException
from ..models.document_model import Document
from ..services.document_service import document_service


logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/", response_model=List[Document])
def get_documents():
    logger.info("GET /documents")
    return document_service.list_documents()

@router.post("/", response_model=Document)
def create_document(document: Document):
    logger.info("POST /documents")
    try:
        return document_service.create_document(document)
    except ValueError as exc:
        logger.error("Failed creating document: %s", exc)
        raise HTTPException(status_code=400, detail=str(exc)) from exc
