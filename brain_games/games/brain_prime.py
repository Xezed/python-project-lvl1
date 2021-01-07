import random
from math import sqrt

from brain_games.engine import play_game

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play_brain_prime():
    play_game(RULES, get_question_with_answer)


def get_question_with_answer() -> tuple:
    number = random.randint(0, 100)
    answer = 'yes' if is_prime(number) else 'no'

    return number, answer


def is_prime(n):
    # 0 and 1 and negatives are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    elif n == 2:
        return True

    # all other even numbers are not primes
    elif n % 2 == 0:
        return False

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers => stride of 2
    sqrt_of_n = int(sqrt(n))
    for x in range(3, sqrt_of_n + 1, 2):
        if n % x == 0:
            return False

    return True
