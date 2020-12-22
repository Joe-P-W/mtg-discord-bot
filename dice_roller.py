import re
import random

from discord.message import Message
from calculator import calculate


async def roll_dice(message: Message):
    channel = message.channel
    content = message.content.replace("/r", "")
    expression = content
    reply = f"{message.author.mention} `{content.replace(' ', '')}` = "

    dice = re.findall(r"(:?\d+)?d(:?\d+)?(:?kh1)?(:?kl1)?", content)

    for die in dice:
        roll_info = parse_rolls(die)
        typed_die = f"{die[0]}d{die[1]}{die[2]}{die[3]}"
        expression = expression.replace(typed_die, roll_info["expression"], 1).strip()
        content = content.replace(typed_die, roll_info["content"], 1).strip()

    reply += f"{content} = {int(calculate(expression))}"

    return await channel.send(reply)


def format_kh1_kl1(return_dict: dict, numbers: list) -> dict:
    return_dict["content"] = "("
    found = False
    for num in numbers:
        if str(num) != return_dict["expression"] and not found:
            found = True
            return_dict["content"] += f'~~{num}~~ ,'
        else:
            return_dict["content"] += f"{num}, "

    return_dict["content"] = return_dict["content"][:-2] + ")"

    return return_dict


def parse_rolls(dice_info: tuple) -> dict:
    return_dict = {}
    numbers = []

    times, die_type, *_ = dice_info

    if not times:
        times = "1"

    for _ in range(int(times)):
        numbers.append(random.randint(1, int(die_type)))

    if dice_info[2]:
        return_dict["expression"] = str(max(numbers))
        return_dict = format_kh1_kl1(return_dict, numbers)

    elif dice_info[3]:
        return_dict["expression"] = str(min(numbers))
        return_dict = format_kh1_kl1(return_dict, numbers)

    else:
        return_dict["expression"] = ""
        for num in numbers:
            return_dict["expression"] += f"{num} + "

        return_dict["expression"] = return_dict["expression"][:-3]
        return_dict["content"] = f"({return_dict['expression']})"

    return return_dict
