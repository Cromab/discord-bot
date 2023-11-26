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
    daily_quote.start()

#Bot commands
@bot.command(name='adventure_card', help='Draw an adventure card.')
async def draw_card(ctx):
    deck = os.getenv('adventure_deck')
    deck = json.loads(deck)
    await ctx.send(random.choice(deck))

@bot.command(name='foundry_roll_dice', help='How to roll custom dice in FoundryVTT')
async def how_to(ctx):
    await ctx.send("""\n
             /r 1d6 -> simple roll
             /r 2d6 -> multiple dice roll
             /r 1d6x -> exploding roll
             /r \{1d6, 1d6\}kh -> keep highest of two or more rolls
             /r 1d6+1 -> roll + constant
             /r {1d6x, 1d8x}kh+4 -> advanced roll
             """)

@bot.command(name="name", help="Generate a random name.")
async def get_name(ctx):
    names = os.getenv('names')
    names = json.loads(names)
    await ctx.send(random.choice(names["name"]) + ' ' + random.choice(names["surname"]))

@bot.command(name="quote", help='Get a random quote.\n To add a new quote: !quote "<new_quote>"')
async def get_quote(ctx, add: str=commands.parameter(default=None, description="Adds a new quote")):
    quotes = os.getenv('quotes')
    quotes = json.loads(quotes)
    if add != None:
        quotes.append(add)
        quotes = json.dumps(quotes)
        set_key(dotenv_file, 'quotes', quotes)
        await ctx.send(f'New Quote: {add}')
    else:
        await ctx.send(random.choice(quotes))

#Bot tasks
@tasks.loop(hours=24)
async def daily_quote():
    message_channel = bot.get_channel(int(os.getenv('discord_channel_id')))
    quotes = os.getenv('quotes')
    quotes = json.loads(quotes)
    await message_channel.send(random.choice(quotes))
@daily_quote.before_loop
async def before_daily_quote():
    print('Waiting...')
    await bot.wait_until_ready()
