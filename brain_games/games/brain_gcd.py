import random

from brain_games.engine import play_game

RULES = 'Find the greatest common divisor of given numbers.'


def play_brain_gcd():
    play_game(RULES, get_question_with_answer)


def get_question_with_answer() -> tuple:
    first_num = random.randint(0, 20)
    second_num = random.randint(0, 20)

    answer = get_correct_answer(first_num, second_num)

    return f'{first_num} {second_num}', answer


def get_correct_answer(first_num, second_num) -> str:
    """Greatest common divisor"""
    while second_num:
        first_num, second_num = second_num, first_num % second_num

    return str(first_num)
