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
    if expression.isdigit():
        return float(expression)

    for operator_symbol in operators:
        left, operator, right = expression.partition(operator_symbol)

        if operator in operators:
            return operators[operator](calculate(left), calculate(right))
