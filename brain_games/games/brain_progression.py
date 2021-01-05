import random

from brain_games.games.play_game import play_game

RULES = 'What number is missing in the progression?'


def play_brain_progression():
    question = get_question()
    answer = get_correct_answer(question)

    play_game(RULES, question, answer)


def get_question():
    initial_number = random.randint(0, 10)
    step = random.randint(1, 6)

    progression = [initial_number]
    for _ in range(1, 10):
        progression.append(progression[-1] + step)

    progression[random.randint(0, 9)] = '..'

    return ' '.join(str(number) for number in progression)


def get_correct_answer(progression_string):
    unknown_number_index = None
    progression_list = progression_string.split(' ')
    for index, number in enumerate(progression_string.split(' ')):
        try:
            progression_list[index] = int(number)
        except ValueError:
            unknown_number_index = index

    # if unknown number in the left hand side of progression
    if unknown_number_index < len(progression_list) / 2:
        progression_step = \
            progression_list[unknown_number_index + 2] - \
            progression_list[unknown_number_index + 1]
        progression_list[unknown_number_index] = \
            progression_list[unknown_number_index + 1] - progression_step
    # otherwise in the right hand side
    else:
        progression_step = \
            progression_list[unknown_number_index - 1] - \
            progression_list[unknown_number_index - 2]
        progression_list[unknown_number_index] = \
            progression_list[unknown_number_index - 1] + progression_step

    return str(progression_list[unknown_number_index])
