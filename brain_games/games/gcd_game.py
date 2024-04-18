from random import randint
import math


def gcd_count():
    a = randint(1, 100)
    b = randint(1, 100)
    exclam = str(a) + ' ' + str(b)
    right_ans = math.gcd(a, b)
    return [right_ans, exclam]


def gcd(func):
    question = 'Find the greatest common divisor of given numbers.'
    func(gcd_count, question)
    return
