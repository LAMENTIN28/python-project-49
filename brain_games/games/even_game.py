from random import randint
from brain_games.engine.engine import check


def even(name):
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    ind = 0
    name = str(name)
    while ind < 3:
        num = randint(1, 999)
        if num % 2 == 0:
            right_ans = 'yes'
        else:
            right_ans = 'no'
        print(f'Question: {num}')
        ans_user = input()
        ind = check(ans_user, right_ans, ind, name)
        if ind is False:
            return
    print('Congratulations, ' + name + "!")
    return
