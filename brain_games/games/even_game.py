from random import randint


def even_count():
    num = randint(1, 999)
    right_ans = 'no'
    if num % 2 == 0:
        right_ans = 'yes'
    exclam = str(num)
    return [right_ans, exclam]


def even(name, func):
    question = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
    func(even_count, name, question)
    return
