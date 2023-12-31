from brain_games.gcd_game import gcd
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    gcd(welcome_user())


if __name__ == '__main__':
    main()