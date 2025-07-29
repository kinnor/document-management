import pytest
from unittest import mock

from backend.app.services.ai_service import generate_summary


def test_generate_summary(monkeypatch):
    monkeypatch.setenv("AI_API_KEY", "key")

    class FakeResponse:
        def __init__(self):
            self.status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            return {"result": "ok"}

    fake_session = mock.MagicMock()
    fake_session.post.return_value = FakeResponse()
    monkeypatch.setattr(
        "backend.app.services.ai_service._create_session", lambda: fake_session
    )

    assert generate_summary("text") == "ok"
    fake_session.post.assert_called()


def test_generate_summary_missing_key(monkeypatch):
    monkeypatch.delenv("AI_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        generate_summary("text")
