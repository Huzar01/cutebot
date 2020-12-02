import os
import discord
import random
from dotenv import load_dotenv
from discord import Member
from discord.ext import commands
from discord import Status
from discord.utils import get
from asyncio import gather


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "COD" in message.content:
        await message.channel.send('Hello!')







client.run(TOKEN)
