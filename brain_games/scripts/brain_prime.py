import brain_games.games.prime_game as prime
from brain_games.engine import start_game


def main():
    start_game(prime.give_data, prime.QUESTION)


if __name__ == '__main__':
    main()
