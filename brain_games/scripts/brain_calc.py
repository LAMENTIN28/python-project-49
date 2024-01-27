#!/usr/bin/env python3

from brain_games.games.calc_game import calc
from brain_games.cli import welcome_user


def main():
    calc(welcome_user())


if __name__ == '__main__':
    main()
