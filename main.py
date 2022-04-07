# ----- Imports ----- #
import discord
import os
import time
from dotenv import load_dotenv
from utils import *
from discord.ext import tasks
# ------------------- #

intents = discord.Intents.all()
client = discord.Client(intents=intents)

prefix = '-'
load_dotenv()
token = os.getenv('TOKEN')
test_token = os.getenv('TEST_TOKEN')

@tasks.loop(seconds=31)
async def daily_ranking_reset():
    if time.strftime('%X')[:-3] == '00:00':
        reset_xp_guilds('daily')

@tasks.loop(hours=13)
async def weekly_ranking_reset():
    if time.strftime('%A') == 'Monday':
        reset_xp_guilds('weekly')

@tasks.loop(hours=13)
async def monthly_ranking_reset():
    if time.strftime('%x').split('/')[1] == '01':
        reset_xp_guilds('monthly')

commands = []

for (dirpath, dirnames, filenames) in os.walk("./commands"):
    for filename in filenames:
        if not filename[-3:] == '.py': continue
        commands.append(filename[:-3])

print("Installed commands:")
for cmd in commands:
    print(f"  {cmd}")

@client.event
async def on_ready():
    daily_ranking_reset.start()
    weekly_ranking_reset.start()
    monthly_ranking_reset.start()

    await client.change_presence(activity=discord.Game(name='rupyy.tk'))
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.author.bot: return
    elif isinstance(message.channel, discord.channel.DMChannel): return

    if message.content.startswith(prefix):
        cmd, args = message.content.split(" ")[0][len(prefix):], message.content.split(" ")[1:]

        if cmd in commands:
            cmdfile = __import__(f"commands.{cmd}", fromlist=[cmd])
            await cmdfile.run(client, message, args)

    else:
        fetchMessages = await message.channel.history(limit=50).flatten()
        counter = 0
        last_messages = []
        message_deleted = False
        for fetchMessage in fetchMessages:
            if counter != 2:
                if fetchMessage.author.id == message.author.id:
                    last_messages.append(fetchMessage)
                    counter += 1
        if len(last_messages) == 2:
            if last_messages[0].content == last_messages[1].content: await message.delete(); message_deleted = True
        
        if not message_deleted:
            xp = 0
            msg_length = len(message.content)

            if msg_length >= 150: xp=150
            elif msg_length >= 100: xp=100
            elif msg_length >= 50: xp=50
            else: xp=msg_length

            add_xp_guild(message.guild.id, xp)
            add_xp_member(message.author.id, message.guild.id, xp)

client.run(token)