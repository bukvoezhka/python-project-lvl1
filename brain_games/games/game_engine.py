"""Common engine for Brain game."""
import prompt


def get_username():
    """Greets player and gets his name.

    Returns:
        username for game session.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def game_session(game_func, check_func, name):
    """
    Create a game session for all of brain games modules.

    Args:
        game_func: main game function of chosen module
        check_func: function for verification player answer
        name: username of player
    """
    count = 0
    while count < 3:
        game_value = game_func()
        print('Question: {0}'.format(game_value))
        player_answer = prompt.string('Your answer: ')
        answer = check_func(game_value)
        if player_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(
                "'{0}' is wrong answer ;(. Correct answer was '{1}'".format(
                    player_answer, answer,
                ),
            )
            print("Let's try again, {0}!".format(name))
            break
        if count == 3:
            print('Congratulations, {0}!'.format(name))
