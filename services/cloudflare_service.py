"""Service for business logic related to Cloudflare DNS management."""

from repositories.cloudflare_repository import CloudflareRepository


class CloudflareService:
    """Service for business logic related to Cloudflare DNS management."""

    def __init__(self, repository: CloudflareRepository):
        self.repository = repository

    def get_zone_id(self, domain: str):
        return self.repository.get_zone_id(domain)

    def list_records(self, domain: str):

        zone_id = self.get_zone_id(domain)

        return self.repository.list_dns_records(zone_id)

    def create_record(
        self,
        domain: str,
        record_type: str,
        name: str,
        content: str,
        ttl=3600,
        proxied=True,
    ):

        zone_id = self.get_zone_id(domain)

        return self.repository.create_dns_record(
            zone_id, record_type, name, content, ttl, proxied
        )

    def delete_record(self, domain: str, record_id: str):

        zone_id = self.get_zone_id(domain)

        return self.repository.delete_dns_record(zone_id, record_id)
