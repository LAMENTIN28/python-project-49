from brain_games.games.gcd_game import gcd
from brain_games.scripts.brain_games import main_brain
from brain_games.engine.engine import engine


def main():
    gcd(main_brain(), engine)


if __name__ == '__main__':
    main()
