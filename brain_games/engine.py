import prompt


def play_game(rules, get_question_wth_answer):
    print('Welcome to the Brain Games!')

    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')

    print(rules)

    for _ in range(3):
        question, correct_answer = get_question_wth_answer()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f' Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {username}!')
            break

    else:
        print(f'Congratulations, {username}!')
