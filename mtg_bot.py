import os

from calculator import calculate
from coin import flip_coin
from dice import roll_dice
from discord.ext import commands


client = commands.Bot(command_prefix="/")


@client.event
async def on_ready():
    print("Bot initialised")


@client.event
async def on_message(message):
    if message.content.startswith("/r"):
        await roll_dice(message)

    elif message.content.startswith("/c"):
        channel = message.channel
        reply = f"{message.author.mention} `{message.content.replace(' ', '').replace('/c', '').strip()}` = "
        reply += str(calculate(message.content.replace("/c", "")))
        await channel.send(reply)

    elif message.content.startswith("/flip"):
        await flip_coin(message)

    elif message.content.startswith("/help") or message.content.startswith("/h"):
        channel = message.channel
        reply = f"{message.author.mention}\n"

        await channel.send(reply)


client.run(os.getenv("mtg_bot_token"))
