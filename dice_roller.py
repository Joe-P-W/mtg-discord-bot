import re
import random

from discord.message import Message
from calculator import calculate


async def roll_dice(message: Message):
    channel = message.channel
    content = message.content.replace("/r", "")
    reply = f"{message.author.mention} `{content.replace(' ', '')}` = "
    reply += " ("

    dice = re.findall(r"\d+d\d+", content)

    rolls = []
    for die in dice:
        times, die_type = die.split("d")
        numbers = []
        for _ in range(int(times)):
            numbers.append(random.randint(1, int(die_type)))

        content.replace(die, str(sum(numbers)), 1)
        rolls += numbers

    for roll in rolls:
        reply += f"{roll} + "

    reply = reply[:-2] + f") = {calculate(content)}"

    return await channel.send(reply)
