from brain_games.calc_game import calc
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    calc(welcome_user())


if __name__ == '__main__':
    main()
