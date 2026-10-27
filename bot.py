import os
import discord
from dotenv import load_dotenv

load_dotenv()

# Strict Environment Variables 
TOKEN = os.getenv("DISCORD_TOKEN")
TARGET_CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True  # Required to read channel text
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Minimalist AI Chat Plugin active as {client.user}")

@client.event
async def on_message(message):
    # Ignore self-loops
    if message.author == client.user:
        return
        
    # Strictly lock execution to your specific Channel ID
    if message.channel.id == TARGET_CHANNEL_ID:
        # Prevent the bot from tripping over empty spaces
        if not message.content:
            return
            
        async with message.channel.typing():
            # Drop-in your choice of lightweight open-source API call here
            ai_response = f"🤖 Processing text: '{message.content}'. (Connect your local LLM hook here!)"
            await message.channel.send(ai_response)

client.run(TOKEN)
