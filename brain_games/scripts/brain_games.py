#!/usr/bin/env python3
"""Brain-game welcome."""
from brain_games.cli import welcome_user


def main():
    """Player greeting."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
