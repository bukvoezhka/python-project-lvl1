"""Game module for brain-even."""
from random import randint

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

START_RANGE = 1
END_RANGE = 100


def start_round():
    """
    Generate random number.

    Returns:
        integer for game session and answer on game.
    """
    number = randint(START_RANGE, END_RANGE)
    is_even = 'yes' if number % 2 == 0 else 'no'
    return number, is_even
