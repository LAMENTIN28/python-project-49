from random import randint


DEFINITION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_answer_question():
    num = randint(1, 999)
    answer = 'yes' if num % 2 == 0 else 'no'
    return answer, str(num)
