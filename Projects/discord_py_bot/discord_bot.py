import os
import discord
import random
from dotenv import load_dotenv
from discord import Member
from discord.ext import commands
from discord import Status
from discord.utils import get
from asyncio import gather
import asyncio
import time
import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client 
client = discord.Client()
# bot
bot = commands.Bot(command_prefix='!')

pharse = ['Hello young thug','Whats up cutie','Im confused why you are talking?', 'I hope your day rocks hard like my whale cock','yea...hey','May you have a wondeful day','1v1 me in simcity','Imagine saying Imagine ']
cod_pharses = ['Pew Pew Pew','Why even play with such a low K/D?','1v1 me bro','I fucked your mom last night while playing COD','Mp5 is OP','WANT TO FUCK WITH TONY HUH?','Imma send Pablo Escabar on your ass','Im going to fuck your father....long dick style']
josh_list = [ 'sounds fair enough' , 'false' , 'you know' , 'comsi comsa' , ' who the fuck is this guy?' , 'I fucked your mom.' , 'FUCK ME?!']
rocket_league_list = ['uhhhh this game????','I dont fuck with those rockets','Just play COD','Eric...............','Matt stop being so cute','Random balls flying everywhere']
love_list = ['awh I love you!','Love everyone here','You are all cute!','**BLUSHES**','Did someone call me handsome?','You da best around, nothings ever going to bring you down ;)']


monty_python = ["There's nothing wrong with you that an expensive operation can't prolong.","My brain hurts!","We use only the finest baby frogs…","Shut up, you American…",
"But kids were different in them days…","Strange women lying in ponds, distributing swords, is no basis for a system of government!",
"He's not the Messiah—he's a very naughty boy!","We interrupt this program to annoy you and make things generally more irritating.",
]

sayings = ['hello','Hello','hey','HEY','hi','say','Hi']
cod_names = ['COD','cod']
sayings_josh = ['fuck','Fuck','FUCK','shit','my','no','yes','chris']
monty_list = ['Monty','monty','nani','snake','python','hack','code','josh']
love_phrases = ['love','laugh','cute','cutie']

myid = '<@171763797856485378>'
johnid = '<@643933956546232320>'
chrisid = '<@657772027532410920>'
joshid = '<@229014637985660929>'


@bot.event
async def on_ready():
    #Change status of bot
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('HuntHunt100'))
    print(f'{bot.user.name} has entered the server')
    print(client)



# REGEX on finding words so it doesn't include 

p = re.compile('ab*')


lock = asyncio.Lock()  # Doesn't require event loop

@bot.event
async def on_message(message):

    phrase_sayings = '(?:% s)' % '|'.join(sayings)
    love_list_sayings = '(?:% s)' % '|'.join(love_phrases)
    phrase_sayings_josh = '(?:% s)' % '|'.join(sayings_josh)
    monty_list_sayings = '(?:% s)' % '|'.join(monty_list)
    if message.author.id == client.user:
        return

    # ignores message that the bot itself sends out
    if message.author.bot: return

    # COD

    if 'cod' in message.content.lower():
        await message.channel.send(random.choice(cod_pharses))
    # greetings
    elif re.match(phrase_sayings,message.content.lower()):
            await message.channel.send(random.choice(pharse))
    # rocket list
    elif 'rocket' in message.content.lower() or 'league' in message.content.lower() or 'rl' in message.content.lower():
        await message.channel.send(random.choice(rocket_league_list))
    # love list
    elif re.match(love_list_sayings, message.content.lower()):
        await message.channel.send(random.choice(love_list))
    # Josh's list
    elif re.match(phrase_sayings_josh,message.content.lower()):
        await message.channel.send(random.choice(josh_list))
    # Monty Python stuff
    elif re.match(monty_list_sayings,message.content.lower()):
        await message.channel.send(random.choice(monty_list))

    # if message.author.id == 171763797856485378:
    # if message.author.id == 643933956546232320:

    # if message.author.id == 229014637985660929:
    #     await message.channel.send(f'SHUT THE FUCK UP {joshid}')
    # if message.author.id == 657772027532410920:
    #    await message.channel.send(f'YO FURY {chrisid}')



    await bot.process_commands(message)



#mute command
@bot.command(name='slience')
async def silence(ctx):
    await ctx.send("silence command is working")
    async with lock:
        await ctx.send('I will shut-up now...')
        await asyncio.sleep(10)
    await ctx.send('I have been released from my cage!')





# test command
@bot.command(name='display', help="A test command that has 3 random lines for stdout")
async def display(ctx):
    test = [
        'This is a test',
        'Second line',
        'Third line'
    ]

    response = random.choice(test)
    await ctx.send(response)

@bot.command(name='review')
async def review(ctx):
    points = [
        'Movie inspired me to become better',
        "Huh? You think I'm a simp like Chirs??",
        "Reminds me of Rebecca Black's Friday"
    ]
    response = random.choice(points)
    await ctx.send(response)

# Rolling dice simulator
@bot.command(name='roll_dice',help='Simulates rolling gangsta dice !roll_dice[# of dice,# of sides]')
async def roll(ctx,number_of_dice:int,number_of_sides:int):
    try:
        dice = [
            str(random.choice(range(1,number_of_sides +1)))
            for _ in range(number_of_dice)
        ]

        await ctx.send(', '.join(dice))
    except:
        await ctx.send('Fool you need to give me the number of dice and how many sides they have')


# Check Member status
# @bot.command(pass_content=True,name='status')
# async def status(ctx, member: Member):
#     await bot.say(str(member.status))
#     await ctx.send(str(member.status))

# Send message to Online Members
@bot.command(name='status')
async def server(ctx, *, text='I see the greatness currently online!'):
    staff = get(ctx.guild.roles, name="CuteBot")
    online = (member for member in staff.members if member.status == Status.online)
    messages = (member.send(text) for member in online)
    await gather(messages)




# Create channel
@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='The-Chosen-Ones'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name.lower())
    print(f'New Channel Name :{existing_channel}')
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

# Welcome new members
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f' Welcome {member.name}, we all know your\'re sexy as hell, get ready to rock and roll young slayer'
    )
    

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command')




bot.run(TOKEN)
