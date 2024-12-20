from adapters.discord_adapter import DiscordAdapter


class DiscordRepository:
    def __init__(self, discord_adapter: DiscordAdapter):
        self.discord_adapter = discord_adapter

    async def get_existing_thread(self, channel, name: str):
        threads = await self.discord_adapter.get_threads(channel)
        for thread in threads:
            if thread.name.lower() == name.lower():
                return thread
        return None

    async def create_thread(self, channel, name: str):
        return await self.discord_adapter.create_thread(channel, name)

    async def get_members_by_ids(self, guild, member_ids: list):
        users = []
        for member_id in member_ids:
            member = await self.discord_adapter.fetch_member(guild, int(member_id))
            if member and not member.bot:
                users.append(member)
        return users

    async def add_users_to_thread(self, thread, users: list):
        for user in users:
            await self.discord_adapter.add_user_to_thread(thread, user)
