#!/usr/bin/env python3
"""Brain-calc game."""
from brain_games import engine
from brain_games.games import calc


def main():
    """Start brain-calc game."""
    engine.run_game(calc)


if __name__ == '__main__':
    main()
