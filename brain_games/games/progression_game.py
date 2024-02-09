from random import randint
from brain_games.engine.engine import engine


def progression_count():
    length = randint(5, 10)
    step = randint(-5, 5)
    first = randint(-10, 10)
    space = ''
    list = []
    count = 1
    while count <= length:
        list.append(first + (step * count))
        count += 1
    space = randint(0, length - 1)
    right_ans = list[space]
    list[space] = ".."
    exclam = str(list)
    exclam = exclam[1:-1]
    return [right_ans, exclam]


def progression(name):
    question = 'What number is missing in the progression?'
    engine(progression_count, name,  question)
    return
