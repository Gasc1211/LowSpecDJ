import os
import discord

# Loading Discord API token
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Bot Startup
client = new discord.Client()


@client.event
async def on_ready():
    print('We\'re Online!')

client.run(token)
