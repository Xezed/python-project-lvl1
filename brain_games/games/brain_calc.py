import random

from brain_games.engine import play_game

GAME_DESCRIPTION = 'What is the result of the expression?'


def play_brain_calc():
    play_game(GAME_DESCRIPTION, get_question_with_answer)


def get_question_with_answer() -> tuple:
    first_operand = random.randint(0, 20)
    second_operand = random.randint(0, 20)
    arithmetic_operation = random.choice('-+*')

    question = f'{first_operand} {arithmetic_operation} {second_operand}'
    answer = get_correct_answer(first_operand,
                                second_operand, arithmetic_operation)

    return question, str(answer)


def get_correct_answer(first_operand, second_operand, arithmetic_operation):
    if arithmetic_operation == '*':
        result = first_operand * second_operand
    elif arithmetic_operation == '+':
        result = first_operand + second_operand
    elif arithmetic_operation == '-':
        result = first_operand - second_operand
    else:
        raise ValueError(f'Unsupported operation: {arithmetic_operation}')

    return result
