from fastapi import FastAPI
from .routes import document_routes, ocr_routes

app = FastAPI(title="Document Management API")

app.include_router(document_routes.router, prefix="/documents", tags=["documents"])
app.include_router(ocr_routes.router, prefix="/ocr", tags=["ocr"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Management API"}
