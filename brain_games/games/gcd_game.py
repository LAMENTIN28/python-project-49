from random import randint
from brain_games.engine.engine import engine
import math


def gcd_count():
    a = randint(1, 100)
    b = randint(1, 100)
    exclam = str(a) + ' ' + str(b)
    right_ans = math.gcd(a, b)
    return [right_ans, exclam]


def gcd(name):
    question = 'Find the greatest common divisor of given numbers.'
    engine(gcd_count, name, question)
    return
