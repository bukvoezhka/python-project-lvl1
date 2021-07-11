"""Game module for brain-even."""
from random import randint

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    """
    Generate random number.

    Returns:
        integer for game session and answer on it.
    """
    question = randint(1, 100)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
