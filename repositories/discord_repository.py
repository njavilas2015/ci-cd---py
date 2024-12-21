from discord import Guild, TextChannel, Thread
from adapters.discord_adapter import DiscordAdapter


class DiscordRepository:
    def __init__(self, discord_adapter: DiscordAdapter):
        """Example"""
        self.discord_adapter = discord_adapter

    async def get_existing_thread(self, channel: TextChannel, name: str):
        """Check if the thread exists"""

        threads = await self.discord_adapter.get_threads(channel)

        for thread in threads:
            if thread.name.lower() == name.lower():
                return thread

        return None

    async def create_thread(self, channel: TextChannel, name: str):
        """Create the thread"""
        return await self.discord_adapter.create_thread(channel, name)

    async def get_members_by_ids(self, guild: Guild | None, member_ids: list):
        """Get members by id, exclude bots"""

        users = []

        for member_id in member_ids:

            member = await self.discord_adapter.fetch_member(guild, int(member_id))

            if member and not member.bot:
                users.append(member)

        return users

    async def add_users_to_thread(self, thread: Thread, users: list):
        """add users to thread"""

        for user in users:
            await self.discord_adapter.add_user_to_thread(thread, user)
