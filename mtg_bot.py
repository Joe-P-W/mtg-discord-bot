import os
import random
import re
from dice_roller import roll_dice
from discord.ext import commands


client = commands.Bot(command_prefix="/")


@client.event
async def on_ready():
    print("Bot initialised")


@client.event
async def on_message(message):
    if message.content.startswith("/r"):
        await roll_dice(message)

    elif message.content.startswith("/flip"):
        channel = message.channel
        reply = f"{message.author.mention} "

        if "until" in message.content:
            fixed_message = message.content.replace("untill", "until")
            loss_condition = fixed_message.split("until")[1].strip().lower()
            with_thumb = False
            proper_command = True
            if loss_condition not in ["heads", "tails"]:
                if "with thumb" in loss_condition:
                    loss_condition = loss_condition.split()[0]
                    with_thumb = True
                    if loss_condition not in ["heads", "tails"]:
                        proper_command = False
                        reply += "you need to choose 'heads' or 'tails' with 'flip until {}' command."
                        await channel.send(reply)
                    else:
                        loss_condition = loss_condition.split()[0], loss_condition.split()[0]
                else:
                    proper_command = False
                    reply += "you need to choose 'heads' or 'tails' with 'flip until {}' command."
                    await channel.send(reply)

            if proper_command:
                wins = 0
                flip = random.choice(["heads", "tails"])
                if with_thumb:
                    flip = flip, random.choice(["heads", "tails"])

                reply += f"\n`{flip}`"

                while flip != loss_condition:
                    wins += 1
                    flip = random.choice(["heads", "tails"])
                    if with_thumb:
                        flip = flip, random.choice(["heads", "tails"])
                    reply += f"\n`{flip}`"

                reply += f"\n`wins = {wins}`"
                await channel.send(reply)

        else:
            channel = message.channel
            reply = f"{message.author.mention} "

            try:
                times = int(re.findall(r"\d+", message.content)[0])
            except IndexError:
                times = 1

            for _ in range(times):
                reply += f"\n`{random.choice(['heads', 'tails'])}`"

            await channel.send(reply)

    elif message.content.startswith("/help") or message.content.startswith("/h"):
        channel = message.channel
        reply = f"{message.author.mention}\n"

        await channel.send(reply)


client.run(os.getenv("mtg_bot_token"))
