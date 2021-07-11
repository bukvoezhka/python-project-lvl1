"""Game module for brain-prime game."""
from math import sqrt
from random import randint

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    """
    Generate random number.

    Returns:
        integer for game session and answer on game.
    """
    question = randint(1, 100)
    answer = is_prime(question)
    return question, answer


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
