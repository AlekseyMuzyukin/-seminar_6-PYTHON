import re

actions = {
    "^": lambda x, y: str(float(x)**float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"


def calculate(expresion: str) -> str:

    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(
            match.group(0), calculate(match.group(1)))

    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(
                match.group(0), action(*match.groups()))

    return expresion


exp = input(str("Введите выражение для вычисления: \n"))
print(calculate(exp))
