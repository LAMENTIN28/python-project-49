from random import randint


def progression_count():
    length = randint(5, 10)
    step = randint(-5, 5)
    first = randint(-10, 10)
    full = ''
    count = 0
    right_ans = ''
    space = randint(0, length - 1)
    while count <= length:
        if count != space:
            full += str(first + (step * count)) + " "
        else:
            full += ".." + " "
            right_ans = str(first + (step * count))
        count += 1
    exclam = full[0:-1]
    return (right_ans, exclam)


def progression():
    QUESTION = 'What number is missing in the progression?'
    print(QUESTION)
    ans = progression_count()
    return ans
