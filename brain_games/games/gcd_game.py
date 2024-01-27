from random import randint
from brain_games.engine.engine import check
import math


def gcd(name):
    ind = 0
    while ind <= 2:
        a = randint(1, 100)
        b = randint(1, 100)
        print('Find the greatest common divisor of given numbers.')
        print(f"Question: {a} {b}")
        right_ans = math.gcd(a, b)
        ans_user = input()
        ind = check(ans_user, right_ans, ind, name)
        if ind is False:
            return
    return
