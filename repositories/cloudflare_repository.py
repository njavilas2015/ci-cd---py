class CloudflareRepository:
    """Repository for handling Cloudflare DNS data."""

    def __init__(self, adapter):
        self.adapter = adapter

    def get_zone_id(self, domain):
        url = f"{self.adapter.base_url}/zones"
        params = {"name": domain}
        data = self.adapter.get(url, params=params)
        if data["success"]:
            return data["result"][0]["id"]
        else:
            raise Exception(f"Error fetching zone ID: {data['errors']}")

    def list_dns_records(self, zone_id):
        url = f"{self.adapter.base_url}/zones/{zone_id}/dns_records"
        data = self.adapter.get(url)
        if data["success"]:
            return data["result"]
        else:
            raise Exception(f"Error listing DNS records: {data['errors']}")

    def create_dns_record(
        self, zone_id, record_type, name, content, ttl=3600, proxied=True
    ):
        url = f"{self.adapter.base_url}/zones/{zone_id}/dns_records"
        payload = {
            "type": record_type,
            "name": name,
            "content": content,
            "ttl": ttl,
            "proxied": proxied,
        }
        data = self.adapter.post(url, payload)
        if data["success"]:
            return data["result"]
        else:
            raise Exception(f"Error creating DNS record: {data['errors']}")

    def delete_dns_record(self, zone_id, record_id):
        url = f"{self.adapter.base_url}/zones/{zone_id}/dns_records/{record_id}"
        data = self.adapter.delete(url)
        if data["success"]:
            return data["result"]
        else:
            raise Exception(f"Error deleting DNS record: {data['errors']}")
