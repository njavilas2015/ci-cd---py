import os
import requests
from typing import Tuple, Any


class ClickUpAdapter:
    """Adapter for interacting with the ClickUp API."""

    API_URL = "https://api.clickup.com/api/v2"
    API_TOKEN = os.getenv("TOKEN_CLICKUP")

    HEADERS = {"Authorization": API_TOKEN}

    @staticmethod
    def put(endpoint: str, data: dict) -> Tuple[int, Any]:
        url = f"{ClickUpAdapter.API_URL}/{endpoint}"
        response = requests.put(url, headers=ClickUpAdapter.HEADERS, json=data)
        return response.status_code, (
            response.json() if response.content else response.text
        )

    @staticmethod
    def get(endpoint: str) -> Tuple[int, Any]:
        url = f"{ClickUpAdapter.API_URL}/{endpoint}"
        response = requests.get(url, headers=ClickUpAdapter.HEADERS)
        return response.status_code, (
            response.json() if response.content else response.text
        )
