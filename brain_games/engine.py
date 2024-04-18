import prompt


def start_game(function, question):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print(question)
    number_right_ans = 3
    for i in range(0, number_right_ans):
        prel = function()
        right_ans = prel[0]
        exclam = prel[1]
        print("Question: " + str(exclam))
        ans_user = input()
        if str(ans_user) == str(right_ans):
            print('Correct!')
            if i == 2:
                print('Congratulations, ' + name + "!")
                return
        else:
            print(str(ans_user) + ' is wrong answer ;(. '
                  'Correct answer was ' + str(right_ans))
            print('Let\'s try again, ' + name + "!")
            return False
    return
