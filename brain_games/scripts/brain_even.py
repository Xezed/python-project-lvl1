from random import randint

from brain_games.games.play_game import play_game


def main():
    play_game(get_question, print_rules, get_correct_answer)


def get_correct_answer(number):
    # is odd
    if int(number) % 2:
        return 'no'
    # is even
    return 'yes'


def print_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_question():
    random_integer = randint(0, 100)
    return random_integer
