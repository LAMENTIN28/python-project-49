import prompt


def start_game(function, CONSTANT):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(CONSTANT)
    round_count = 3
    for _ in range(0, round_count):
        right_ans, exclam = function()
        print("Question: " + str(exclam))
        ans_user = prompt.string("")
        if str(ans_user) != str(right_ans):
            print(str(ans_user) + ' is wrong answer ;(. '
                  'Correct answer was ' + str(right_ans))
            print('Let\'s try again, ' + name + "!")
            return
        print('Correct!')
    print('Congratulations, ' + name + "!")
