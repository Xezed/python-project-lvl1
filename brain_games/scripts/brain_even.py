from random import randint


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
