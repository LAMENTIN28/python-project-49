from brain_games.progression_game import progression
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    progression(welcome_user())


if __name__ == '__main__':
    main()
