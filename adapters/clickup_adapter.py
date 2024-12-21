"""Adapter for interacting with the ClickUp API."""

import os
from typing import Tuple, Any
from requests import Response
import requests


class ClickUpAdapter:
    """Adapter for interacting with the ClickUp API."""

    API_URL: str = "https://api.clickup.com/api/v2"
    API_TOKEN: str = os.getenv("TOKEN_CLICKUP")

    HEADERS: dict[str, str] = {"Authorization": API_TOKEN}

    @staticmethod
    def put(endpoint: str, data: dict) -> Tuple[int, Any]:
        """Update the cards"""
        url: str = f"{ClickUpAdapter.API_URL}/{endpoint}"

        response: Response = requests.put(
            url, headers=ClickUpAdapter.HEADERS, json=data, timeout=10
        )

        return response.status_code, (
            response.json() if response.content else response.text
        )

    @staticmethod
    def get(endpoint: str) -> Tuple[int, Any]:
        """Obtain information from the cards"""

        url: str = f"{ClickUpAdapter.API_URL}/{endpoint}"

        response: Response = requests.get(
            url, headers=ClickUpAdapter.HEADERS, timeout=10
        )

        return response.status_code, (
            response.json() if response.content else response.text
        )
