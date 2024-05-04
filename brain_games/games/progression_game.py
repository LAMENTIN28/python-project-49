from random import randint


DEFINITION = 'What number is missing in the progression?'


def get_answer_exclam():
    length = randint(5, 10)
    step = randint(-5, 5)
    first = randint(-10, 10)
    full = ''
    count = 0
    right_ans = ''
    space = randint(0, length - 1)
    while count <= length:
        if count != space:
            full += f'{(first + (step * count))} '
        else:
            full += ".." + ' '
            right_ans = str(first + (step * count))
        count += 1
    exclam = full[0:-1]
    return right_ans, exclam
