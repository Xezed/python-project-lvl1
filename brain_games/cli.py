"""CLI functions."""
import argparse

import prompt

from brain_games.scripts.brain_games import play_game


def welcome_user():
    """Prompting for user name and greeting him with it."""
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')

    return name


def main(game_name):
    username = welcome_user()
    play_game(username, game_name)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--name',
        help='Game name',
        type=str
    )

    args = parser.parse_args()

    main(args.name)
