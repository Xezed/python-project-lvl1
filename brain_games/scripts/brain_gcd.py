import random
from math import gcd

from brain_games.games.play_game import play_game


def main():
    play_game(get_question, print_rules, get_correct_answer)


def get_question():
    first_num = random.randint(0, 20)
    second_num = random.randint(0, 20)

    return f'{first_num} {second_num}'


def print_rules():
    print('Find the greatest common divisor of given numbers.')


def get_correct_answer(string_of_numbers):
    first_num_str, second_num_str = string_of_numbers.split(' ')
    first_num_int, second_num_int = int(first_num_str), int(second_num_str)

    return str(gcd(first_num_int, second_num_int))
