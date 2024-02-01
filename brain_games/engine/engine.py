def check(ans_user, right_ans, ind, name):
    if str(ans_user) == str(right_ans):
        print('Correct!')
        new_ind = ind + 1
        if new_ind == 3:
            print('Congratulations, ' + name + "!")
        return new_ind
    else:
        print(str(ans_user) + ' is wrong answer ;(. '
              'Correct answer was ' + str(right_ans))
        print('Let\'s try again, ' + name + "!")
        return False


def questions(question):
    print(question)
    return

def quest_exclam(exclam):
    print("Question: " + exclam)
    return
