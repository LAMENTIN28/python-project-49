from random import randint
from brain_games.engine.engine import check


def calc(name):
    ind = 0
    print("What is the result of the expression?")
    while ind <= 2:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        sign = randint(1, 3)
        if sign == 1:
            print("Question: " + str(num1) + " + " + str(num2))
            right_ans = num1 + num2
        elif sign == 2:
            print("Question: " + str(num1) + " - " + str(num2))
            right_ans = num1 - num2
        elif sign == 3:
            print("Question: " + str(num1) + " * " + str(num2))
            right_ans = num1 * num2
        print("Your answer is: ")
        ans_user = input()
        ind = check(ans_user, right_ans, ind, name)
        if ind is False:
            return
    return
