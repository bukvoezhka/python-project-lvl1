"""Game module for brain-prime game."""
from math import sqrt
from random import randint

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

START_RANGE = 1
END_RANGE = 100


def start_round():
    """
    Generate game data.

    Returns:
        integer for game session and answer on game.
    """
    number = randint(START_RANGE, END_RANGE)
    return number, is_prime(number)


def is_prime(number):
    """
    Check the number.

    Args:
        number: random integer.

    Returns:
        prime check answer.
    """
    if number == 2:
        return 'yes'
    if number % 2 == 0:
        return 'no'
    devider = int(sqrt(number)) + 1
    while devider > 2:
        if number % devider == 0:
            return 'no'
        devider -= 1
    return 'yes'
