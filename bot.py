#bot.py

import os

import discord
from discord import user
from discord import channel
intents = discord.Intents.default()
intents.members = True
intents.messages = True

from dotenv import load_dotenv

#load_dotenv loads variables from .env file into you environment variables
    #via the getenv methods below
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#client is an object that represents a connection to discord
client = discord.Client(intents=intents)

#on_ready is an event handler that is activated once the connections to discord
#   has been established by Client and it has finished perparing the data
#   that discord has initially sent (login state, guild, channel data, etc)
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break


    #keyword 'f' at beginning of literal string allows you to insert variables
    #   without quotes, etc.
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, Welcome! This is a test.'
    )

@client.event
async def on_message(message):
    if (client.user == message.author):
        return
    else:
        channel=client.get_channel()
        await channel.send("message has been sent")

        

client.run(TOKEN)
