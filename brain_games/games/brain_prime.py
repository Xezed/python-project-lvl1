import random

from brain_games.games.play_game import play_game

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play_brain_prime():
    question = get_question()
    answer = get_correct_answer(question)
    play_game(RULES, question, answer)


def get_question():
    number = random.randint(0, 100)
    return f'{number}'


def get_correct_answer(number_as_string):
    number = int(number_as_string)

    # Is prime number?
    for i in range(3, number):
        if number % i == 0:
            return 'no'
    return 'yes'
