def engine(function, name, question):
    print(question)
    ind = 0
    while ind < 3:
        prel = function()
        right_ans = prel[0]
        exclam = prel[1]
        print("Question: " + str(exclam))
        ans_user = input()
        if str(ans_user) == str(right_ans):
            print('Correct!')
            ind +=1
            if ind == 3:
                print('Congratulations, ' + name + "!")
                return
        else:
            print(str(ans_user) + ' is wrong answer ;(. '
              'Correct answer was ' + str(right_ans))
            print('Let\'s try again, ' + name + "!")
            return False
    return
