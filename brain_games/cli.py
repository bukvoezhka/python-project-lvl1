"""CLI game module."""
import prompt


def welcome_user():
    """Player name query."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


if __name__ == 'main':
    welcome_user()
