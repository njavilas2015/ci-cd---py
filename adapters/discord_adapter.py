import discord


class DiscordAdapter:
    """Adapter for interacting with the ClickUp API."""

    async def fetch_member(self, guild, member_id: int):
        try:
            return await guild.fetch_member(member_id)
        except Exception as e:
            return None

    async def create_thread(self, channel, name: str):
        return await channel.create_thread(
            name=name, type=discord.ChannelType.private_thread
        )

    async def get_threads(self, channel):
        return channel.threads

    async def add_user_to_thread(self, thread, user):
        await thread.add_user(user)
