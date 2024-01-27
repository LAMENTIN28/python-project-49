from random import randint
from brain_games.engine.engine import check


def gcd(name):
    ind = 0
    while ind <= 2:
        a = randint(1, 100)
        b = randint(1, 100)
        print('Find the greatest common divisor of given numbers.')
        print(f"Question: {a} {b}")
        e = 1
        while e <= a and e <= b:
            if a % e == 0 and b % e == 0:
                right_ans = e
            e += 1
        ans_user = input()
        ind = check(ans_user, right_ans, ind, name)
        if ind is False:
            return
    return
