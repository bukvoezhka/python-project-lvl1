#!/usr/bin/env python3
"""Main game module."""
from brain_games.cli import welcome_user


def main():
    """Player greeting."""
    print('Welcome to the Brain Games!')  ## noqa WPS421
    welcome_user()


if __name__ == '__main__':
    main()
