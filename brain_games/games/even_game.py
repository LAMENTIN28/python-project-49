from random import randint
from brain_games.engine.engine import engine


def even_count():
    num = randint(1, 999)
    right_ans = 'no'
    if num % 2 == 0:
        right_ans = 'yes'
    exclam = str(num)
    return [right_ans, exclam]


def even(name):
    question = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
    engine(even_count, name, question)
    return
