#bot.py
import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

#client 
client = discord.Client()
# bot
from discord.ext import commands
bot = commands.Bot(command_prefix='!')

pharse = ('Hello young thug','Whats up cutie','Im confused why you are talking?', 'I hope your day rocks hard like my whale cock','yea...hey')
cod_pharses = ('Pew Pew Pew','Why even play with such a low K/D?','1v1 me bro','I fucked your mom last night while playing COD','Mp5 is OP','WANT TO FUCK WITH TONY HUH?')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has entered the server')

@bot.command(name='display')
async def display(ctx):
    test = [
        'This is a test',
        'Second line',
        'Third line'
    ]

    response = random.choice(test)
    await ctx.send(response)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

# async def on_message(message):
    if message.content.startswith("hello"):
        await message.channel.send(random.choice(pharse))
    elif 'raise-exception' in message.content:
        raise discord.DiscordException 

    cod = "COD"
    # if message.content(cod.lower()):
    if cod.lower() in message.content:
        await message.channel.send(random.choice(cod_pharses))
    if cod in message.content:
        await message.channel.send(random.choice(cod_pharses))

@client.event
#Error logdfd
async def on_error(event, *args, **kwargs):
    with open('err.log','a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise 

# Welcome new members
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f' Welcome {member.name}, we all know your\'re sexy as hell, get ready to rock and roll young slayer'
    )
    

client.run(TOKEN)
