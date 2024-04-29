import brain_games.games.progression_game as progression
from brain_games.engine import start_game


def main():
    start_game(progression.give_data, progression.QUESTION)


if __name__ == '__main__':
    main()
