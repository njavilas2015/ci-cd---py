"""Adapter for interacting with the ClickUp API."""

from typing import List
import discord
from discord import Guild, Member, TextChannel, Thread


class DiscordAdapter:
    """Adapter for interacting with the ClickUp API."""

    async def fetch_member(self, guild: Guild | None, member_id: int) -> Member:
        """Gets member data"""
        return await guild.fetch_member(member_id)

    async def create_thread(self, channel: TextChannel, name: str) -> Thread:
        """Create thread in channel"""
        return await channel.create_thread(
            name=name, type=discord.ChannelType.private_thread
        )

    async def get_threads(self, channel: TextChannel) -> List[Thread]:
        """Get information from the thread"""
        return channel.threads

    async def add_user_to_thread(self, thread: Thread, user) -> None:
        """Add users to thread"""
        await thread.add_user(user)
