# Document Management API

This project provides a small document management service built with
[FastAPI](https://fastapi.tiangolo.com/). It exposes a REST API for storing
document metadata, extracting text from uploaded PDFs and generating summaries
via an external AI service. A simple React frontend is included for uploading
files and viewing results.

## Features

- CRUD style endpoints for storing document metadata in memory
- OCR extraction using **Tesseract** through `pdf2image` and `pytesseract`
- AI summarisation by calling an external API
- Dockerfile for containerised deployments
- React frontend powered by **Vite**

## Requirements

- Python 3.11+
- Node.js (for the frontend)
- Tesseract OCR installed on the host machine

The backend dependencies are listed in `requirements.txt`. The tests require the
same packages.

## Setup

Clone the repository and install the Python requirements. If `virtualenv` or a
similar tool is available, create an isolated environment first.

```bash
git clone <repo-url>
cd document-management
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The application reads two environment variables when calling the AI service:

- `AI_API_KEY` &ndash; API key for the external provider
- `AI_API_URL` &ndash; optional override for the API endpoint

## Running the Backend

Start the API locally with Uvicorn:

```bash
uvicorn backend.app.main:app --reload
```

The server listens on <http://localhost:8000> by default.

### Tests

Run the unit and integration tests with `pytest` from the repository root:

```bash
pytest
```

## Frontend

The `frontend` directory holds a standalone React application. To launch the
development server:

```bash
cd frontend
npm install
npm run dev
```

Set the `VITE_API_URL` environment variable if the backend runs on another URL.

## Docker Deployment

To build and run the API as a container:

```bash
docker build -t document-api .
docker run -p 8000:8000 document-api
```

The Docker image installs the Python dependencies and runs the FastAPI
application on port `8000`.

