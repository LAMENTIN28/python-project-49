#!/usr/bin/env python3

from brain_games.games.progression_game import progression
from brain_games.cli import welcome_user


def main():
    progression(welcome_user())


if __name__ == '__main__':
    main()
