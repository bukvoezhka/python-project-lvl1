"""Brain-calc game."""
from brain_games.games import calc, engine


def main():
    """Start brain-calc game."""
    engine.run_game(calc)


if __name__ == '__main__':
    main()
