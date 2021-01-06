import random

from brain_games.engine import play_game

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play_brain_prime():
    play_game(RULES, get_question_with_answer)


def get_question_with_answer() -> tuple:
    number = random.randint(0, 100)
    answer = get_correct_answer(number)
    return number, answer


def get_correct_answer(number_as_string):
    number = int(number_as_string)

    # Is prime number?
    for i in range(3, number):
        if number % i == 0:
            return 'no'
    return 'yes'
