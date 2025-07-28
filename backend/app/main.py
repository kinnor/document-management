from fastapi import FastAPI
from .routes import document_routes

app = FastAPI(title="Document Management API")

app.include_router(document_routes.router, prefix="/documents", tags=["documents"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Management API"}
