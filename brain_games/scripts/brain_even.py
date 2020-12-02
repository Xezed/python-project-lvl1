from random import randint

import prompt

from brain_games.cli import welcome_user


def main():
    username = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_amount = 0

    while correct_answers_amount != 3:
        random_integer = randint(0, 100)

        user_answer = prompt.string(f'Question: {random_integer} ')
        print(f'Your answer: {username}')
        correct_answer = get_correct_answer(random_integer)

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


def get_correct_answer(number):
    # is odd
    if int(number) % 2:
        return 'no'
    # is even
    return 'yes'


if __name__ == '__main__':
    main()
