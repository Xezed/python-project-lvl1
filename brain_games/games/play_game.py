import prompt

from brain_games.games.welcome_user import welcome_user


def play_game(get_question, print_rules, get_correct_answer):
    username = welcome_user()

    print_rules()

    for _ in range(3):
        question = get_question()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')
        correct_answer = get_correct_answer(question)

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f' Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {username}!')
            break

    else:
        print(f'Congratulations, {username}!')
