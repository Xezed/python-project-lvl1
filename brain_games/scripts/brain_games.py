import prompt

from brain_games.scripts import brain_calc, brain_even, brain_gcd, brain_progression

GAMES = {
    'brain-even': {
        'get_question': brain_even.get_question,
        'print_rules': brain_even.print_rules,
        'get_correct_answer': brain_even.get_correct_answer,
    },
    'brain-calc': {
        'get_question': brain_calc.get_question,
        'print_rules': brain_calc.print_rules,
        'get_correct_answer': brain_calc.get_correct_answer,
    },
    'brain-gcd': {
        'get_question': brain_gcd.get_question,
        'print_rules': brain_gcd.print_rules,
        'get_correct_answer': brain_gcd.get_correct_answer,
    },
    'brain-progression': {
        'get_question': brain_progression.get_question,
        'print_rules': brain_progression.print_rules,
        'get_correct_answer': brain_progression.get_correct_answer,
    },
}


def play_game(username, game_name):
    correct_answers_amount = 0

    try:
        game_function_set = GAMES[game_name]
    except KeyError:
        print('Game does not exist.')
        return

    while correct_answers_amount != 3:
        question = game_function_set['get_question']()

        game_function_set['print_rules']()
        user_answer = prompt.string(f'Question: {question} ')
        print(f'Your answer: {username}')
        correct_answer = game_function_set['get_correct_answer'](question)

        if user_answer == correct_answer:
            correct_answers_amount += 1
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f' Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {username}!')

            # streak has been ended
            correct_answers_amount = 0

    print(f'Congratulations, {username}!')
