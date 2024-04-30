from random import randint


DEFINITION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_answer_exclam():
    num = randint(1, 999)
    right_ans = 'no'
    if num % 2 == 0:
        right_ans = 'yes'
    exclam = str(num)
    return right_ans, exclam
