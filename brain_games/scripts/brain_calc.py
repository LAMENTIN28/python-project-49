from brain_games.games.calc_game import calc
from brain_games.scripts.brain_games import main_brain
from brain_games.engine.engine import engine


def main():
    calc(main_brain(), engine)


if __name__ == '__main__':
    main()
