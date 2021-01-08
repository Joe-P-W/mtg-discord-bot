import asyncio
import re
from typing import Union
from operator import pow, truediv, mul, add, sub

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '^': pow
}


async def calculate(expression: str) -> Union[float, int, str]:
    await asyncio.sleep(0.01)
    loop = asyncio.get_event_loop()

    while "(" in expression or ")" in expression:
        if expression.count(")") != expression.count("("):
            return "Uneven brackets"
        await asyncio.sleep(0.01)

        bracketed_expressions = re.findall(r"\([0-9-*\/^+. ]+\)", expression)
        for bracketed_expression in bracketed_expressions:
            expression = expression.replace(
                bracketed_expression,
                str(await loop.create_task(calculate(bracketed_expression[1:-1]))),
                1
            )
            await asyncio.sleep(0.01)

    if expression.replace(".", "", 1).strip().isdigit():
        if expression[-2:] == ".0":
            return int(expression[:-2])
        elif "." not in expression:
            return int(expression)
        else:
            return float(expression)

    for operator_symbol in operators:
        left, operator, right = expression.partition(operator_symbol)

        if operator in operators:
            try:
                return operators[operator](
                    await loop.create_task(calculate(left.strip())),
                    await loop.create_task(calculate(right.strip()))
                )
            except ZeroDivisionError:
                return "Tried to divide by 0"
