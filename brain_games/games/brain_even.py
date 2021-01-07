from random import randint

from brain_games.engine import play_game

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_brain_even():
    play_game(RULES, get_question_with_answer)


def get_question_with_answer() -> tuple:
    random_integer = randint(0, 100)
    answer = 'yes' if is_even(random_integer) else 'no'
    return random_integer, answer


def is_even(number):
    if int(number) % 2:
        return False
    else:
        return True
