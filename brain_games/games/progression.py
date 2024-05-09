from random import randint


DEFINITION = 'What number is missing in the progression?'


def get_answer_question():
    length = randint(5, 10)
    step = randint(1, 10)
    first = randint(-10, 10)
    full = ''
    answer = ''
    space_number = randint(0, length - 1)
    last = first + (step * length)
    full = list(range(first, last, step))
    answer = full[space_number]
    full[space_number] = ".."
    return answer, str(full).replace("'", '')[1:-1]
