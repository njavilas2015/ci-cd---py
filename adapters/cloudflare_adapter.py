"""Adapter for interacting with the Cloudflare API."""

import requests
from requests import Response


class CloudflareAdapter:
    """Adapter for interacting with the Cloudflare API."""

    def __init__(self, token: str):
        self.base_url = "https://api.cloudflare.com/client/v4"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def validate(self, url: str, params=None):
        """check if the current token is valid"""
        response: Response = requests.get(
            url, headers=self.headers, params=params, timeout=10
        )
        return response.json()

    def get(self, url: str, params=None):
        """Adapter GET"""
        response: Response = requests.get(
            url, headers=self.headers, params=params, timeout=10
        )
        return response.json()

    def post(self, url: str, payload: dict[str, str]):
        """Adapter POST"""
        response: Response = requests.post(
            url, json=payload, headers=self.headers, timeout=10
        )
        return response.json()

    def delete(self, url: str):
        """Adapter DELETE"""
        response: Response = requests.delete(url, headers=self.headers, timeout=10)
        return response.json()
