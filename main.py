import os
import discord
from discord.ext import commands
from discord import app_commands

from services.discord_thread_service import DiscordThreadService
from services.task_service import ClickUpTaskService
from services.cloudflare_service import CloudflareService

from adapters.discord_adapter import DiscordAdapter
from adapters.clickup_adapter import ClickUpAdapter
from adapters.cloudflare_adapter import CloudflareAdapter

from repositories.discord_repository import DiscordRepository
from repositories.task_repository import ClickUpTaskRepository
from repositories.cloudflare_repository import CloudflareRepository


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

discord_adapter = DiscordAdapter()
discord_repository = DiscordRepository(discord_adapter)
thread_service = DiscordThreadService(discord_repository)


@bot.event
async def on_ready():
    print(f"Connected as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synchronized {len(synced)} commands.")
    except Exception as e:
        print(f"Error synchronizing commands: {e}")


@bot.tree.command(name="testing", description="Request fixture test")
async def testing(interaction: discord.Interaction):
    await thread_service.testing(interaction)


@bot.tree.command(name="fixture", description="Create new fixture")
@app_commands.describe(
    id="ID fixture",
)
async def create_thread(interaction: discord.Interaction, id: str, members: str):
    await thread_service.create_thread(interaction, id, members)


bot.run(os.getenv("TOKEN_DISCORD"))


if __name__ == "__main__":

    API_TOKEN = "your_api_token_here"
    DOMAIN = "example.com"

    adapter = CloudflareAdapter(API_TOKEN)
    repository = CloudflareRepository(adapter)
    service = CloudflareService(repository)

    try:
        # List DNS records
        records = service.list_records(DOMAIN)
        print("Current DNS Records:")
        for record in records:
            print(f"- {record['type']} {record['name']} -> {record['content']}")

        # Create a new DNS record
        new_record = service.create_record(
            DOMAIN, "A", "subdomain.example.com", "123.123.123.123"
        )
        print(f"Created DNS Record: {new_record}")

        # Delete the DNS record
        record_id = new_record["id"]
        service.delete_record(DOMAIN, record_id)
        print(f"Deleted DNS Record with ID: {record_id}")

    except Exception as e:
        print(str(e))

    ID_LISTA = "tu_id_lista_aquí"

    task_service = ClickUpTaskService()

    tasks = task_service.get_tasks(ID_LISTA)

    if tasks:
        print("Tareas obtenidas:")
        for task in tasks:
            print(f"- {task['name']} (ID: {task['id']})")
    else:
        print("No se encontraron tareas o hubo un error.")
