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


def calculate(expression: str) -> Union[float, int]:

    if "(" in expression and ")" in expression:
        for _ in range(expression.count("(") - 1):
            x = re.findall(r"\([0-9-*\/^+. ]+\)", expression)
            for bracketed_expression in x:
                expression = expression.replace(bracketed_expression, str(calculate(bracketed_expression[1:-1])), 1)

    if expression.replace(".", "", 1).strip().isdigit():
        return float(expression)

    for operator_symbol in operators:
        left, operator, right = expression.partition(operator_symbol)

        if operator in operators:
            return operators[operator](calculate(left.strip()), calculate(right.strip()))
