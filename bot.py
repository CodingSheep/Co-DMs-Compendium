import asyncio
import discord
import os

from discord.ext import commands


# Setup
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix='!')

@client.event
async def setup_hook() -> None:
    for cog in os.listdir('./cogs'):
        if cog.endswith('.py'):
            extension = f'cogs.{cog[:-3]}'
            print(f'Loading Extension: {extension}...')
            await client.load_extension(extension)


# Run the Discord bot
client.run(os.environ['DISCORD_KEY'])