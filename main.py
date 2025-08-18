import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot logado como {client.user}")

TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
