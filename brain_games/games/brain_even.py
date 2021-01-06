from random import randint

from brain_games.engine import play_game

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_brain_even():
    play_game(RULES, get_question_with_answer)


def get_question_with_answer() -> tuple:
    random_integer = randint(0, 100)
    answer = get_correct_answer(random_integer)
    return random_integer, answer


def get_correct_answer(number):
    # is odd
    if int(number) % 2:
        return 'no'
    # is even
    return 'yes'
