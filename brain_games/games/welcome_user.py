import prompt


def welcome_user():
    """Prompting for user name and greeting him with it."""
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    return name
