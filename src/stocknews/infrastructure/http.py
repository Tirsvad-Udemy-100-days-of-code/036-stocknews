"""Minimal JSON over HTTP client built on the standard library."""

import json
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Mapping
from typing import Any

from stocknews.domain.errors import ApiError


def open_url(url: str, timeout: float) -> bytes:
    """Read the body of a URL.

    @param url The full URL, query string included.
    @param timeout Seconds to wait for the answer.
    @return The raw response body.
    """
    with urllib.request.urlopen(url, timeout=timeout) as response:
        body: bytes = response.read()
    return body


def get_json(
    url: str, params: Mapping[str, str | int], timeout: float
) -> dict[str, Any]:  # JSON objects are untyped by nature
    """Fetch a JSON object with a GET request.

    The URL is never put in an error message, because it holds API keys.

    @param url The endpoint without a query string.
    @param params The query parameters.
    @param timeout Seconds to wait for the answer.
    @return The decoded JSON object.
    @throws ApiError on a network, HTTP or decoding failure.
    """
    full_url = f"{url}?{urllib.parse.urlencode(params)}"
    try:
        data = json.loads(open_url(full_url, timeout))
    except ValueError as error:
        raise ApiError("the answer is not valid JSON") from error
    except OSError as error:
        raise ApiError(f"request failed: {error}") from error
    if not isinstance(data, dict):
        raise ApiError("the answer is not a JSON object")
    return data
