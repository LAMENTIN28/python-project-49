from random import randint
from brain_games.engine.engine import check


def progression(name):
    ind = 0
    print("What number is missing in the progression?")
    while ind <= 2:
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
        q = "Question:"
        print(q, *list)
        ans_user = input()
        ind = check(ans_user, right_ans, ind, name)
        if ind is False:
            return
    print('Congratulations, ' + name + "!")
    return
