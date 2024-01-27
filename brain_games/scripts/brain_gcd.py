from brain_games.games.gcd_game import gcd
from brain_games.cli import welcome_user


def main():
    gcd(welcome_user())


if __name__ == '__main__':
    main()
