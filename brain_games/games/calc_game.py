from random import randint
from operator import sub, add, mul


def calc_count():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    sign = randint(0, 2)
    operators_sym = ['+', '-', '*']
    operators = [add, sub, mul]
    exclam = str(num1) + ' ' + operators_sym[sign] + ' ' + str(num2)
    right_ans = operators[sign](num1, num2)
    return (right_ans, exclam)


def calc():
    QUESTION = "What is the result of the expression?"
    print(QUESTION)
    ans = calc_count()
    return ans
