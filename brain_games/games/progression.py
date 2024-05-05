from random import randint


DEFINITION = 'What number is missing in the progression?'


def get_answer_exclam():
    length = randint(5, 10)
    step = randint(-5, 5)
    first = randint(-10, 10)
    full = ''
    right_ans = ''
    space_number = randint(0, length - 1)
    last = first + (step * length)
    for k, v in enumerate(range(first, last, step)):
        if k != space_number:
            full += f'{(first + (step * k))} '
        else:
            full += ".." + ' '
            right_ans = str(first + (step * k))
    exclam = full[0:-1]
    return right_ans, exclam
