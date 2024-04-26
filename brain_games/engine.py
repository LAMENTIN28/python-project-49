import prompt


def start_game(function):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    right_ans_count = 3
    for i in range(0, right_ans_count):
        right_ans, exclam = function()
        print("Question: " + str(exclam))
        ans_user = prompt.string("")
        if str(ans_user) == str(right_ans):
            print('Correct!')
        else:
            print(str(ans_user) + ' is wrong answer ;(. '
                  'Correct answer was ' + str(right_ans))
            print('Let\'s try again, ' + name + "!")
            return False
    print('Congratulations, ' + name + "!")
    return
