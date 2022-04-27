#!/usr/bin/env python3
"""Brain-even game."""
from brain_games import engine
from brain_games.games import even


def main():
    """Start brain-even game."""
    engine.run_game(even)


if __name__ == '__main__':
    main()
