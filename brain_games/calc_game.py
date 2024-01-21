from random import randint


def calc(name):  # noqa: C901
    i = 0
    print("What is the result of the expression?")
    while i <= 2:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        sign = randint(1, 3)
        if sign == 1:
            print("Question: " + str(num1) + " + " + str(num2))
            ans = num1 + num2
            print("Your answer is: ")
            ansu = input()
            if str(ans) == ansu:
                i += 1
                print('Correct!')
            else:
                print(str(ansu) + ' is wrong answer ;(. '
                      'Correct answer was ' + str(ans))
                print('Try again, ' + name)
                return
        elif sign == 2:
            print("Question: " + str(num1) + " - " + str(num2))
            ans = num1 - num2
            print("Your answer is: ")
            ansu = input()
            if str(ans) == ansu:
                i += 1
                print('Correct!')
            else:
                print(str(ansu) + ' is wrong answer ;(. '
                      'Correct answer was ' + str(ans))
                print('Try again, ' + name)
                return
        elif sign == 3:
            print("Question: " + str(num1) + " * " + str(num2))
            ans = num1 * num2
            print("Your answer is: ")
            ansu = input()
            if str(ans) == ansu:
                i += 1
                print('Correct!')
            else:
                print(str(ansu) + ' is wrong answer ;(. '
                      'Correct answer was ' + str(ans))
                print('Let\'s try again, ' + name)
                return
    print('Congratulations, ' + name + "!")
    return
