"""Game module for brain-progression game."""
from random import randint

GAME_RULES = 'What number is missing in the progression?'

START_LENGHT_LIST = 6
END_LENGHT_LIST = 10

START_NUMBER = 3
END_NUMBER = 11

START_STEP = 2
END_STEP = 7


def start_round():
    """
    Generate a random arithmetic progression for game session.

    Returns:
        progression with random empty value for solution and answer on game.
    """
    sequence = generate_progression()
    hiden_value = randint(1, len(sequence) - 1)
    answer = sequence[hiden_value]
    sequence[hiden_value] = '..'
    return ' '.join(map(str, sequence)), str(answer)


def generate_progression():
    """
    Generate a random arithmetic progression.

    Returns:
        list of progression.
    """
    progression = []
    progression_lenght = randint(START_LENGHT_LIST, END_LENGHT_LIST)
    progression_value = randint(START_NUMBER, END_NUMBER)
    progression_step = randint(START_STEP, END_STEP)
    progression.append(progression_value)
    for _ in range(progression_lenght):
        progression_value += progression_step
        progression.append(progression_value)
    return progression
