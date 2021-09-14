import discord, os, asyncio, datetime, requests

from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)

async def on_ready():
    client.remove_command('help')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("TESTING"))

client.run('NjcwNTIyMjU2NjgxNTk4OTk2.YUA_IA.wbhx_ET1e8nFU1qptsVpZpmUMjQ', bot=False)
