import os
import sys, traceback

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Below cogs represents our folder our cogs are in.
initial_extensions = ['cogs.music']

bot = commands.Bot(command_prefix='!')