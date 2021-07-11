"""Game module for brain-progression game."""
from random import randint

GAME_RULES = 'What number is missing in the progression?'


def main():
    """
    Generate a random arithmetic progression for game session.

    Returns:
        progression with random empty value for solution and correct answer.
    """
    question = generate_progression()
    hide_value = randint(1, len(question) - 1)
    answer = question.pop(hide_value)
    question.insert(hide_value, '..')
    return ' '.join(question), answer


def generate_progression():
    """
    Generate a random arithmetic progression.

    Returns:
        list of progression.
    """
    lenght_list = randint(5, 10)
    start_number = randint(1, 15)
    step = randint(2, 6)
    progression = []
    progression.append(str(start_number))
    for _ in range(lenght_list):
        start_number += step
        progression.append(str(start_number))
    return progression
