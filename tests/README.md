# Tests

This project uses **pytest** for all unit and integration tests. Install the
requirements from `requirements.txt` and run the suite from the repository root:

```bash
pip install -r requirements.txt
pytest
```

Test files cover the following components:

- `test_document_service.py` &ndash; unit tests for the in-memory document store.
- `test_ai_service.py` &ndash; unit tests for the AI API integration.
- `test_ocr_service.py` &ndash; unit tests for the OCR helpers.
- `test_app.py` &ndash; integration tests for the FastAPI routes.

Each test is documented with docstrings explaining its purpose.
