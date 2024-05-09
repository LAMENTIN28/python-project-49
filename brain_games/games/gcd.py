from random import randint
import math


DEFINITION = 'Find the greatest common divisor of given numbers.'


def get_answer_question():
    a = randint(1, 100)
    b = randint(1, 100)
    question = f'{a} {b}'
    answer = math.gcd(a, b)
    return answer, question
