from __future__ import annotations

"""Integration with external AI API."""

from typing import Any
import logging
import os

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)

API_URL = os.getenv("AI_API_URL", "https://api.example.com/v1/generate")


def _create_session(retries: int = 3, backoff_factor: float = 0.5) -> requests.Session:
    """Create a requests session with retry strategy."""
    retry_strategy = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["POST"],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def generate_summary(text: str, timeout: float = 5.0) -> str:
    """Send text to the external AI API and return the generated summary."""
    api_key = os.getenv("AI_API_KEY")
    if not api_key:
        raise RuntimeError("AI_API_KEY not configured")

    session = _create_session()
    headers = {"Authorization": f"Bearer {api_key}"}
    logger.info("Sending text to AI API")
    try:
        response = session.post(API_URL, json={"text": text}, headers=headers, timeout=timeout)
        response.raise_for_status()
    except requests.Timeout as exc:
        logger.error("AI API request timed out: %s", exc)
        raise RuntimeError("AI API request timed out") from exc
    except requests.RequestException as exc:
        logger.error("AI API request failed: %s", exc)
        raise RuntimeError(f"AI API request failed: {exc}") from exc

    try:
        data = response.json()
    except ValueError as exc:
        logger.error("Invalid AI API response: %s", exc)
        raise RuntimeError("Invalid AI API response") from exc

    logger.debug("AI API response: %s", data)
    result = data.get("result")
    if result is None:
        logger.error("AI API response missing 'result': %s", data)
        raise RuntimeError("AI API response missing 'result'")

    logger.info("AI API summary generated")
    return str(result)
