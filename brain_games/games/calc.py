"""Game module for brain-calc."""
from operator import add, mul, sub
from random import choice, randint

GAME_RULES = 'What is the result of the expression?'
OPERATOR = {  ## noqa WPS407
    '+': add,
    '-': sub,
    '*': mul,
}


def main():
    """
    Generate a random expression for game.

    Returns:
        exrpession to solve and answer on it.
    """
    num1 = randint(1, 35)
    num2 = randint(1, 35)
    op = choice(list(OPERATOR.keys()))
    question = '{0} {1} {2}'.format(num1, op, num2)
    answer = '{0}'.format(OPERATOR[op](num1, num2))
    return question, answer
