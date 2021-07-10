"""Common engine for Brain game."""
import prompt


def game_session(game_func, verify_func, game_rule):
    """
    Create a 3-round game session for all of brain games modules.

    Args:
        game_func: main game function of chosen module
        verify_func: function for verification player answer
        game_rule: current rule of game session.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game_rule)
    game_round = range(3)
    for _ in game_round:
        game_value = game_func()
        print('Question: {0}'.format(game_value))
        player_answer = prompt.string('Your answer: ')
        answer = verify_func(game_value)
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
