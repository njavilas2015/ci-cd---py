import discord
from discord.ext import commands
from discord import app_commands

from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)


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

    if not isinstance(interaction.channel, discord.TextChannel):
        await interaction.response.send_message(
            "This command can only be run on a text channel."
        )

    print(interaction.channel.name)

    if interaction.channel.name != "developers":
        await interaction.response.send_message(
            "This command can only be used in a specific channel.", ephemeral=True
        )
        return

    # thread = interaction.message.thread.id

    await interaction.response.send_message(
        f"You have run the /testing command!", ephemeral=True
    )

    await interaction.followup.send(f"Create environment sandbox", ephemeral=True)


@bot.tree.command(name="fixture", description="Create new fixture")
@app_commands.describe(
    id="ID fixture",
)
async def create_thread(interaction: discord.Interaction, id: str, members: str):

    name: str = f"fixture/{id}"

    if not isinstance(interaction.channel, discord.TextChannel):
        await interaction.response.send_message(
            "This command can only be run on a text channel."
        )

    member_ids = [id.strip("<@!>") for id in members.replace(",", " ").split()]

    if not member_ids:
        await interaction.response.send_message(
            "Please mention at least one user."
        )
        return

    existing_thread = None

    for thread in interaction.channel.threads:
        if thread.name.lower() == name.lower():
            existing_thread = thread
            break

    if existing_thread is not None:

        await interaction.response.send_message(
            f"There is already a thread with the name '{name}'.", ephemeral=True
        )

        return

    thread = await interaction.channel.create_thread(
        name=f"fixture/{id}",
        type=discord.ChannelType.private_thread,
    )

    users = []

    for member_id in member_ids:
        try:
            member = await interaction.guild.fetch_member(int(member_id))

            if not member.bot:
                users.append(member)

        except Exception as e:
            await interaction.channel.send(f"Error  {member_id}: {e}")

    await thread.add_user(member)

    await thread.send(
        f"¡Hola! Los he añadido a este hilo para hacer el seguimiento de la tarea {name}. Por favor, revisen los detalles y actualicen el progreso aquí. Si tienen alguna pregunta, no duden en comunicarse. Asegúrense de mantener el código limpio y modular para facilitar futuras mejoras."
    )

    await interaction.response.send_message(f"Created new thread {name}!")


bot.run(os.getenv("TOKEN_DISCORD"))
