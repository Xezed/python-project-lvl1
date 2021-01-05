import prompt


def main():
    print('Welcome to the Brain Games!')

    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')


if __name__ == '__main__':
    main()
