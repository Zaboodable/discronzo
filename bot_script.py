token = open("token.txt", 'r').read()

import discord
from discord.ext import tasks

import time
import datetime
from datetime import datetime

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord')

date_to_ring = datetime(2022, 2, 25, 12, 0, 0)

@tasks.loop(seconds=60)
async def bot_loop(bot):
    global date_to_ring
    await bot.wait_until_ready()
    date_now = datetime.now()
    date_diff = date_to_ring - date_now
    hours = (date_diff.days * 24) + (date_diff.seconds // 3600)
    presence_text = f'{hours} hours to Elden Ring'
    game = discord.Game(name=presence_text)
    await bot.change_presence(status=discord.Status.online ,activity=game)

bot_loop.start(bot)
bot.run(token)

