#bot.py

#imports
import os
import discord
import json

from discord import user
from discord import channel
from dotenv import load_dotenv

#set intents so bot will have proper access to discord data
intents = discord.Intents.default()
intents.members = True
intents.messages = True

#load environment variables from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#Load channel ids from dotenv - must be cast to int
TESTING1 = int(os.getenv('CHANNELS_TESTING1'))
TESTING2 = int(os.getenv('CHANNELS_TESTING2'))

#open data file
with open('raffleData.json') as datafile:
    data = json.load(datafile)

#client is an object that represents a connection to discord
client = discord.Client(intents=intents)

#on_ready is an event handler that is activated once the connections to discord
#   has been established by Client and it has finished perparing the data
#   that discord has initially sent (login state, guild, channel data, etc)
@client.event
async def on_ready():

    #testbed code
    for guild in client.guilds:

        if guild.name == GUILD:
            break

    #test bed code
    #keyword 'f' at beginning of literal string allows you to insert variables
    #   without quotes, etc.
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )

    #get channel ids
    # for channel in client.get_all_channels():
    #     print(f'Channel {channel.name} id is {channel.id}')

    #testbed code
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

#test bed code
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, Welcome! This is a test.'
    )

#search user messages for raffle entries as messages are sent
@client.event
async def on_message(message):

    #define keyword for searching message contents
    keyword = '#raffle'

    if (client.user == message.author):
        return

    else:

        #verify message comes from appropriate channel and mentions keyword
        if((message.channel.id==TESTING1) and (message.content.find(keyword)!=-1)):

            #relay message to moderated channel for review
            channel = client.get_channel(TESTING2)
            await channel.send(f'Raffle Entry Submitted For Approval:\n\nMessage ID: {message.id}\nMessage User: {message.author}\n```Contents:\n{message.content}\n```')


#search for moderator approvals of raffle entries
@client.event
async def on_raw_reaction_add(reaction):

    #need to inspect reactions ONLY of raffle entries copied into secure channel

    #display reaction
    print(reaction.emoji)
         

client.run(TOKEN)
