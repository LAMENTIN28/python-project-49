import prompt


def start_game(game_module):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.DEFINITION)
    round_count = 3
    for _ in range(0, round_count):
        right_ans, exclam = game_module.get_answer_question()
        print(f'Question: {exclam}')
        ans_user = prompt.string("")
        if str(ans_user) != str(right_ans):
            print(f'{ans_user} is wrong answer ;(. '
                  f'Correct answer was {right_ans}')
            print(f'Let\'s try again, {name}!')
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
