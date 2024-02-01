from random import randint
from brain_games.engine.engine import check, questions, quest_exclam


def prime(name):
    ind = 0
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions(question)
    def repeat():
        i = 2
        count = 0
        number = randint(1, 1000)
        exclam = f"{number}"
        quest_exclam(exclam)
        right_ans = 'yes'
        while i < number:
            if number % i == 0:
                count += 1
                right_ans = "no"
            i += 1
        ans_user = input()
        ind = check(ans_user, right_ans, ind, name)
        if ind is False:
            return
    return
