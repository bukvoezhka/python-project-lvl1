"""Brain-calc game."""
from brain_games.games.game_calc import brain_calc, find_result
from brain_games.games.game_engine import game_session


def main():
    """Brain calculation game."""
    game_rule = 'What is the result of the expression?'
    game_session(brain_calc, find_result, game_rule)


if __name__ == '__main__':
    main()
