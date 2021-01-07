import random

from brain_games.engine import play_game

RULES = 'What number is missing in the progression?'


def play_brain_progression():
    play_game(RULES, get_question_with_answer)


def get_question_with_answer() -> tuple:
    initial_number = random.randint(0, 10)
    step = random.randint(1, 6)

    progression = [initial_number]

    progression_length = 10

    # first element in the list already
    for _ in range(1, progression_length):
        last_element = progression[-1]
        progression.append(last_element + step)

    unknown_number_index = random.randint(0, 9)
    progression[unknown_number_index] = '..'

    question = ' '.join(str(number) for number in progression)
    answer = initial_number + step * unknown_number_index

    return question, answer
