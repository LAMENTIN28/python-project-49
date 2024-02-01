from random import randint
from brain_games.engine.engine import check, questions, quest_exclam
from operator import sub, add, mul


def calc(name):
    ind = 0
    question = "What is the result of the expression?"
    questions(question)
    while ind < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        sign = randint(0, 2)
        operators_sym = ['+', '-', '*']
        operators = [add, sub, mul]
        exclam = str(num1) + ' ' + operators_sym[sign] + ' ' + str(num2)
        quest_exclam(exclam)
        right_ans = operators[sign](num1, num2)
        ans_user = input()
        ind = check(ans_user, right_ans, ind, name)
        if ind is False:
            return
    return
