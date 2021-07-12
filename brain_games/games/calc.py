"""Game module for brain-calc."""
from operator import add, mul, sub
from random import choice, randint

GAME_RULES = 'What is the result of the expression?'

OPERATORS = {  ## noqa WPS407
    '+': add,
    '-': sub,
    '*': mul,
}

START_RANGE = 1
END_RANGE = 35


def start_round():
    """
    Generate a random expression for game.

    Returns:
        exrpession to solve and answer on game.
    """
    number1 = randint(START_RANGE, END_RANGE)
    number2 = randint(START_RANGE, END_RANGE)
    sign, operation = choice(list(OPERATORS.items()))
    return (
        '{0} {1} {2}'.format(number1, sign, number2),
        '{0}'.format(operation(number1, number2)),
    )
