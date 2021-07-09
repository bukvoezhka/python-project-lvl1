"""Game module for brain-calc."""
from random import choice, randint

operator = (' + ', ' - ', ' * ')


def brain_calc():
    """
    Generate a random expression for game.

    Returns:
        expression to solve.
    """
    num1 = str(randint(1, 35))  ## noqa S311
    num2 = str(randint(1, 35))  ## noqa S311
    return num1 + choice(operator) + num2  ## noqa S311


def find_result(expression):
    """
    Solves expression for brain-calc game.

    Args:
        expression: random expression generate by brain_calc.

    Returns:
        correct answer.
    """
    expression = expression.split(' ')
    num1 = int(expression[0])
    num2 = int(expression[2])
    if '+' in expression:
        return str(num1 + num2)
    if '-' in expression:
        return str(num1 - num2)
    return str(num1 * num2)
