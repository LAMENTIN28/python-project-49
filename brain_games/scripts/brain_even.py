import brain_games.games.even_game as even
from brain_games.engine import start_game


def main():
    start_game(even.give_data, even.QUESTION)


if __name__ == '__main__':
    main()
