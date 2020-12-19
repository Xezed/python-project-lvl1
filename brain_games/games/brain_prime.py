import random


def get_question():
    number = random.randint(0, 100)
    return f'{number}'


def print_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_correct_answer(number_as_string):
    number = int(number_as_string)

    # Is prime number?
    for i in range(3, number):
        if number % i == 0:
            return 'no'
    return 'yes'
