import brain_games.games.gcd_game as gcd
from brain_games.engine import start_game


def main():
    start_game(gcd.give_data, gcd.QUESTION)


if __name__ == '__main__':
    main()
