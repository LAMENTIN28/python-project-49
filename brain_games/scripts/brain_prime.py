from brain_games.games.prime_game import prime
from brain_games.scripts.brain_games import main_brain
from brain_games.engine.engine import engine


def main():
    prime(main_brain(), engine)


if __name__ == '__main__':
    main()
