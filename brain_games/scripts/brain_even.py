from brain_games.even_game import even
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    even(welcome_user())


if __name__ == '__main__':
    main()
