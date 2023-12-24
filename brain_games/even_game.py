from random import randint


def even(name):
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    i = 0
    name = str(name)
    while i < 3:
        num = randint(1, 999)
        print(num)
        ans = input()
        if num % 2 == 0 and ans == "yes":
            i += 1
            print("Corect!")
        elif num % 2 != 0 and ans == "no":
            i += 1
            print('Corect!')
        elif num % 2 != 0 and ans == "yes":
            print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.'
                  ' Let\'s try again, ' + name + "!")
            return
        elif num % 2 == 0 and ans == "no":
            print('\'no\' is wrong answer ;(. Correct answer was \'yes\'.'
                  ' Let\'s try again, ' + name + "!")
            return
        else:
            print(ans + ' is wrong answer ;(.'
                  ' Choose \'yes\' or \'no\'. Let\'s try again, ' + name + "!")
            return
    print('Congratulations, ' + name + "!")
    return
