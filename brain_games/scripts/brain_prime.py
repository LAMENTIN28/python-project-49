#!/usr/bin/env python3

from brain_games.games.prime_game import prime
from brain_games.cli import welcome_user


def main():
    prime(welcome_user())


if __name__ == '__main__':
    main()
