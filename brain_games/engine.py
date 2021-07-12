"""Common engine for Brain game."""
import prompt

GAME_ROUNDS = 3


def run_game(brain_game):
    """
    Create a 3-round game session for all of brain games modules.

    Args:
        brain_game: game module of choosen game.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(brain_game.GAME_RULES)
    for _ in range(GAME_ROUNDS):
        question, answer = brain_game.start_round()
        print('Question: {0}'.format(question))
        player_answer = prompt.string('Your answer: ')
        if player_answer != answer:
            print(
                "'{0}' is wrong answer ;(. Correct answer was '{1}'".format(
                    player_answer, answer,
                ),
            )
            print("Let's try again, {0}!".format(name))
            break
        print('Correct!')
    else:
        print('Congratulations, {0}!'.format(name))
