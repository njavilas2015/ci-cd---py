"""Repository for handling Cloudflare DNS data."""

from adapters.cloudflare_adapter import CloudflareAdapter


class CloudflareRepository:
    """Repository for handling Cloudflare DNS data."""

    def __init__(self, adapter: CloudflareAdapter):
        """Example"""
        self.adapter = adapter

    def get_zone_id(self, domain: str):
        """Example"""
        url: str = f"{self.adapter.base_url}/zones"

        params: dict[str, str] = {"name": domain}

        data = self.adapter.get(url, params=params)

        if data["success"]:
            return data["result"][0]["id"]

        raise Exception(f"Error fetching zone ID: {data['errors']}")

    def list_dns_records(self, zone_id: str):
        """Example"""

        url: str = f"{self.adapter.base_url}/zones/{zone_id}/dns_records"

        data = self.adapter.get(url)

        if data["success"]:
            return data["result"]

        raise Exception(f"Error listing DNS records: {data['errors']}")

    def create_dns_record(
        self,
        zone_id: str,
        record_type: str,
        name: str,
        content: str,
        ttl=3600,
        proxied=False,
    ):
        """Example"""

        url: str = f"{self.adapter.base_url}/zones/{zone_id}/dns_records"

        payload: dict[str, str] = {
            "type": record_type,
            "name": name,
            "content": content,
            "ttl": ttl,
            "proxied": proxied,
        }

        data = self.adapter.post(url, payload)

        if data["success"]:
            return data["result"]

        raise Exception(f"Error creating DNS record: {data['errors']}")

    def delete_dns_record(self, zone_id: str, record_id: str):
        """Example"""

        url: str = f"{self.adapter.base_url}/zones/{zone_id}/dns_records/{record_id}"

        data = self.adapter.delete(url)

        if data["success"]:
            return data["result"]

        raise Exception(f"Error deleting DNS record: {data['errors']}")

    def validate(self):
        """Example"""

        url: str = f"{self.adapter.base_url}/user/tokens/verify"

        data = self.adapter.get(url)

        if data["success"]:
            return data["result"]

        raise Exception(f"Error validate token: {data['errors']}")
