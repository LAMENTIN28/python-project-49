from random import randint
import math


DEFINITION = 'Find the greatest common divisor of given numbers.'


def get_answer_exclam():
    a = randint(1, 100)
    b = randint(1, 100)
    exclam = str(a) + ' ' + str(b)
    right_ans = math.gcd(a, b)
    return right_ans, exclam
