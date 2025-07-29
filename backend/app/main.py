import logging
from fastapi import FastAPI
from .routes import document_routes, ocr_routes, ai_routes

logger = logging.getLogger(__name__)

app = FastAPI(title="Document Management API")

app.include_router(document_routes.router, prefix="/documents", tags=["documents"])
app.include_router(ocr_routes.router, prefix="/ocr", tags=["ocr"])
app.include_router(ocr_routes.router, tags=["ocr"])
app.include_router(ai_routes.router, prefix="/ai", tags=["ai"])

@app.get("/")
def read_root():
    logger.info("GET /")
    return {"message": "Welcome to the Document Management API"}
