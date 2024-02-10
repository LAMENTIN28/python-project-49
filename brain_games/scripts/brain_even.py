from brain_games.games.even_game import even
from brain_games.scripts.brain_games import main_brain
from brain_games.engine.engine import engine


def main():
    even(main_brain(), engine)


if __name__ == '__main__':
    main()
