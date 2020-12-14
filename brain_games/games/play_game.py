import prompt

from brain_games.games.welcome_user import welcome_user


def play_game(get_question, print_rules, get_correct_answer):
    correct_answers_amount = 0
    username = welcome_user()

    while correct_answers_amount != 3:
        question = get_question()

        print_rules()
        user_answer = prompt.string(f'Question: {question} ')
        print(f'Your answer: {user_answer}')
        correct_answer = get_correct_answer(question)

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
