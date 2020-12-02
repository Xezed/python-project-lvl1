"""CLI functions."""
import prompt


def welcome_user():
    """Prompting for user name and greeting him with it."""
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
