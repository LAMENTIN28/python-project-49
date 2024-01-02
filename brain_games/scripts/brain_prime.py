from brain_games.prime_game import prime
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    prime(welcome_user())


if __name__ == '__main__':
    main()
