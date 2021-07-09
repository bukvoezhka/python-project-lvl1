"""Brain-calc game."""
from brain_games.games.game_calc import brain_calc, find_result
from brain_games.games.game_engine import game_session, get_username


def main():
    """Brain calculation game."""
    name = get_username()
    print('What is the result of the expression?')
    game_session(brain_calc, find_result, name)


if __name__ == '__main__':
    main()
