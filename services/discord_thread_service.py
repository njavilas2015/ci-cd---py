from repositories.discord_repository import DiscordRepository
from discord import Interaction, TextChannel


class DiscordThreadService:
    def __init__(self, discord_repository: DiscordRepository):
        self.discord_repository = discord_repository

    async def testing(self, interaction: Interaction):
        if not isinstance(interaction.channel, TextChannel):
            await interaction.response.send_message(
                "This command can only be run on a text channel."
            )
            return

        if interaction.channel.name != "developers":
            await interaction.response.send_message(
                "This command can only be used in a specific channel.", ephemeral=True
            )
            return

        await interaction.response.send_message(
            f"You have run the /testing command!", ephemeral=True
        )

        await interaction.followup.send(f"Create environment sandbox", ephemeral=True)

    async def create_thread(self, interaction: Interaction, id: str, members: str):
        name = f"fixture/{id}"

        if not isinstance(interaction.channel, TextChannel):
            await interaction.response.send_message(
                "This command can only be run on a text channel."
            )
            return

        member_ids = [id.strip("<@!>") for id in members.replace(",", " ").split()]

        if not member_ids:
            await interaction.response.send_message("Please mention at least one user.")
            return

        existing_thread = await self.discord_repository.get_existing_thread(
            interaction.channel, name
        )
        if existing_thread:
            await interaction.response.send_message(
                f"There is already a thread with the name '{name}'.", ephemeral=True
            )
            return

        thread = await self.discord_repository.create_thread(interaction.channel, name)
        users = await self.discord_repository.get_members_by_ids(
            interaction.guild, member_ids
        )

        await self.discord_repository.add_users_to_thread(thread, users)

        await thread.send(
            f"¡Hola! Los he añadido a este hilo para hacer el seguimiento de la tarea {name}. Por favor, revisen los detalles y actualicen el progreso aquí. Si tienen alguna pregunta, no duden en comunicarse. Asegúrense de mantener el código limpio y modular para facilitar futuras mejoras."
        )

        await interaction.response.send_message(f"Created new thread {name}!")
