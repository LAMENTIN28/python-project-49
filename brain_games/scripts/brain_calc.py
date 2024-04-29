import brain_games.games.calc_game as calc
from brain_games.engine import start_game


def main():
    start_game(calc.give_data, calc.QUESTION)


if __name__ == '__main__':
    main()
