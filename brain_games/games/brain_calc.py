import random

from brain_games.games.play_game import play_game

RULES = 'What is the result of the expression?'


def play_brain_calc():
    question = get_question()
    answer = get_correct_answer(question)
    play_game(RULES, question, answer)


def get_question():
    first_operand = random.randint(0, 20)
    second_operand = random.randint(0, 20)
    arithmetic_operation = random.choice('-+*')

    return f'{first_operand} {arithmetic_operation} {second_operand}'


def get_correct_answer(expression):
    # to follow the same logic as per other games. Surely we could avoid it.
    expr_without_spaces = expression.replace(' ', '')
    first_operand, arithmetic_operation, second_operand = expr_without_spaces
    first_operand, second_operand = int(first_operand), int(second_operand)

    if arithmetic_operation == '*':
        result = first_operand * second_operand
    elif arithmetic_operation == '+':
        result = first_operand + second_operand
    elif arithmetic_operation == '-':
        result = first_operand - second_operand
    else:
        raise ValueError('Unsupported operation')

    return result
