import requests
from requests import Response


class CloudflareAdapter:
    """Adapter for interacting with the Cloudflare API."""

    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://api.cloudflare.com/client/v4"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }

    def get(self, url, params=None):
        response: Response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def post(self, url, payload):
        response: Response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def delete(self, url):
        response: Response = requests.delete(url, headers=self.headers)
        return response.json()
