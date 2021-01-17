from random import randint

from brain_games.engine import play_game

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_brain_even():
    play_game(GAME_DESCRIPTION, get_question_with_answer)


def get_question_with_answer() -> tuple:
    question = randint(0, 100)
    answer = 'yes' if is_even(question) else 'no'
    return question, str(answer)


def is_even(number):
    return (int(number) % 2) == 0
