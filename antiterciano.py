import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True
client = Client(command_prefix="!", intents=intents)


TERCIANO_ID = discord.Object(id=497657958591627274)  # 👈 ID del usuario objetivo


@client.tree.command(name="kick", description="Exiliar a Terciano de los canales de voz")
async def kickTerciano(interaction: discord.Interaction):
    await interaction.response.send_message()

client.run(os.getenv("DISCORD_TOKEN"))
