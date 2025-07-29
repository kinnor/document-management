# Document Management API

This repository contains a minimal FastAPI application for managing documents.
It now includes basic OCR functionality using Tesseract and pdf2image.

## Features

- Create and list document metadata.
- Extract text from uploaded PDF files via the `/ocr/extract` or `/extract` endpoints.
- Generate AI summaries via the `/ai/generate` endpoint.

## Development

Install dependencies from `requirements.txt` and run the tests with `pytest`.

## Frontend

The `frontend` directory contains a standalone React application built with
[Vite](https://vitejs.dev/). Install its dependencies with `npm install` and
start the development server:

```bash
cd frontend
npm install
npm run dev
```

The source code is organized into `components`, `pages`, `services` and `utils`
for a clean separation from the backend.
