from random import randint
from brain_games.engine.engine import check


def prime(name):
    ind = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while ind <= 2:
        i = 2
        count = 0
        number = randint(1, 1000)
        print(f"Question: {number}")
        while i < number:
            if number % i == 0:
                count += 1
            i += 1
        if count == 0:
            right_ans = "yes"
        else:
            right_ans = "no"
        ans_user = input()
        ind = check(ans_user, right_ans, ind, name)
        if ind is False:
            return
    print('Congratulations, ' + name + "!")
    return
