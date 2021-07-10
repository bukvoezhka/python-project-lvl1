"""Brain-even game."""
from brain_games.games.game_engine import game_session
from brain_games.games.game_even import brain_even, is_even


def main():
    """Brain even game."""
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_session(brain_even, is_even, game_rule)


if __name__ == '__main__':
    main()
