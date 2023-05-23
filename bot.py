import discord
import os
from dotenv import load_dotenv
import requests
load_dotenv()

# intents = discord.Intents.default()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("https://www.chess.com"):
        response = requests.post("https://8382ok6h0f.execute-api.us-east-2.amazonaws.com/test/review", json={"link": message.content})
        if response.status_code == 200:
            await message.channel.send("Reviewed!")

client.run(os.getenv("TOKEN"))
