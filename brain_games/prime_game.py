from random import randint


def prime(name):
    ind = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while ind <= 2:
        i = 2
        count = 0
        number = randint(1, 1000)
        print(f"Question: {number}")
        while i < number:
            if number % i == 0:
                count += 1
            i += 1
        if count == 0:
            right_ans = "yes"
        else:
            right_ans = "no"
        ans_user = input()
        if right_ans == ans_user:
            print('Correct!')
            ind += 1
        else:
            print(str(ans_user) + ' is wrong answer ;(. '
                  'Correct answer was ' + str(right_ans))
            return
    print('Congratulations, ' + name + "!")
    return
