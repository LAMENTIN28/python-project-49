from random import randint


DEFINITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_answer_exclam():
    number = randint(1, 1000)
    exclam = f"{number}"
    right_ans = check_number(number)
    right_ans = 'yes' if check_number(number) is True else 'no'
    return right_ans, exclam

def check_number(number):
    i = 2
    while i < number:
        right_ans = False if number % i == 0 else True
        if right_ans is False:
            return right_ans
        i += 1
    return right_ans
