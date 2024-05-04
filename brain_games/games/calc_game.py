from random import randint
from operator import sub, add, mul


DEFINITION = "What is the result of the expression?"


def get_answer_exclam():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    sign = randint(0, 2)
    operators_sym = ['+', '-', '*']
    operators = [add, sub, mul]
    exclam = f'{num1} {operators_sym[sign]} {num2}'
    right_ans = operators[sign](num1, num2)
    return right_ans, exclam
