from random import randint

from brain_games.games.play_game import play_game

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_brain_even():
    question = get_question()
    answer = get_correct_answer(question)
    play_game(RULES, question, answer)


def get_correct_answer(number):
    # is odd
    if int(number) % 2:
        return 'no'
    # is even
    return 'yes'


def get_question():
    random_integer = randint(0, 100)
    return random_integer
