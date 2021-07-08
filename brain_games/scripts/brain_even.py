"""Brain-even game module."""
import random

import prompt


def main():
    """Brain even game."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        random_number = random.randint(1, 100)  ## noqa WPS 311
        print('Question: {0}'.format(random_number))
        player_answer = input('Your answer: ')
        answer = is_even(random_number)
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


def is_even(number):
    """
    Сhecks the parity of a number for brain-even game.

    Args:
        number (int): random number.

    Returns:
        str: Correct answer.
    """
    return 'yes' if number % 2 == 0 else 'no'


if __name__ == '__main__':
    main()
