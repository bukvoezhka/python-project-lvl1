"""Game module for brain-even."""
from random import randint


def brain_even():
    """
    Generate random number.

    Returns:
        integer for game session.
    """
    return randint(1, 100)  ## noqa S311


def is_even(number):
    """
    Сhecks the parity of a number for brain-even game.

    Args:
        number (int): random number.

    Returns:
        correct answer.
    """
    return 'yes' if number % 2 == 0 else 'no'
