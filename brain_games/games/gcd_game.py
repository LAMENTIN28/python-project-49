from random import randint
from brain_games.engine.engine import check, questions, quest_exclam
import math


def gcd(name):
    ind = 0
    def repeat():
        a = randint(1, 100)
        b = randint(1, 100)
        question = 'Find the greatest common divisor of given numbers.'
        questions(question)
        exclam = str(a) + ' ' + str(b)
        quest_exclam(exclam)
        right_ans = math.gcd(a, b)
        ans_user = input()
        ind = check(ans_user, right_ans, ind, name)
        if ind is False:
            return
    return
