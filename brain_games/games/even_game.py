from random import randint
from brain_games.engine.engine import check, questions, quest_exclam


def even(name):
    question = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
    questions(question)
    ind = 0
    name = str(name)
    def repeat():
        num = randint(1, 999)
        right_ans = 'no'
        if num % 2 == 0:
            right_ans = 'yes'
        exclam = str(num)
        quest_exclam(exclam)
        ans_user = input()
        ind = check(ans_user, right_ans, ind, name)
        if ind is False:
            return
    return
