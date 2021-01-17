import random

from brain_games.engine import play_game

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def play_brain_gcd():
    play_game(GAME_DESCRIPTION, get_question_with_answer)


def get_question_with_answer() -> tuple:
    first_num = random.randint(0, 20)
    second_num = random.randint(0, 20)

    question = f'{first_num} {second_num}'
    answer = get_greatest_common_divisor(first_num, second_num)

    return question, str(answer)


def get_greatest_common_divisor(first_num, second_num):
    while second_num:
        first_num, second_num = second_num, first_num % second_num

    return first_num
