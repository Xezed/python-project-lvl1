import random

from simpleeval import simple_eval

from brain_games.games.play_game import play_game


def play_brain_calc():
    play_game(get_question, print_rules, get_correct_answer)


def get_question():
    first_operand = random.randint(0, 20)
    second_operand = random.randint(0, 20)
    operation = random.choice('-+*')

    return f'{first_operand} {operation} {second_operand}'


def print_rules():
    print('What is the result of the expression?')


def get_correct_answer(arithmetic_operation):
    int_result = simple_eval(arithmetic_operation)
    str_result = str(int_result)
    return str_result
