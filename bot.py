import os
import random
import discord
import json
from dotenv import load_dotenv, find_dotenv, set_key
from discord.ext import commands

#Load environment variables
dotenv_file = find_dotenv()
load_dotenv()
token = os.getenv('discord_token')
guild = os.getenv('discord_guild')
guild_channel = os.getenv('discord_guild_id')

#Declare intents
intents = discord.Intents.default()
intents.message_content = True

#Bot instantiation
bot = commands.Bot(command_prefix='!', intents=intents)

#Bot connection confirmation
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('5e'))
    print(f'{bot.user.name} has connected to Discord!')

#Bot commands
@bot.command(name="quote", help='Get a random quote.\n To add a new quote: !quote "<new_quote>"')
async def get_quote(ctx, add: str=commands.parameter(default=None, description="Adds a new quote")):
    quotes = os.getenv('quotes')
    quotes = quotes.split(' :: ')
    if add != None:
        quotes.append(add)
        quotes =' :: '.join(quotes)
        set_key(dotenv_file, 'quotes', quotes)
        await ctx.send(f'New Quote: {add}')
    else:
        await ctx.send(random.choice(quotes))

@bot.command(name="name", help="Generate a random name.")
async def get_name(ctx):
    names = os.getenv(name)
