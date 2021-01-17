import random

from brain_games.engine import play_game

GAME_DESCRIPTION = 'What number is missing in the progression?'


def play_brain_progression():
    play_game(GAME_DESCRIPTION, get_question_with_answer)


def get_question_with_answer() -> tuple:
    initial_number = random.randint(0, 10)
    step = random.randint(1, 6)

    progression = []
    progression_length = 10

    # first element in the list already
    for index in range(progression_length):
        if index == 0:
            progression.append(initial_number)
        else:
            progression.append(progression[index - 1] + step)

    unknown_number_index = random.randint(0, progression_length - 1)
    progression[unknown_number_index] = '..'

    question = ' '.join(str(number) for number in progression)
    answer = initial_number + step * unknown_number_index

    return question, str(answer)
