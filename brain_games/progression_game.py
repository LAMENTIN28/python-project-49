from random import randint


def progression(name):
    right_ans = 0
    print("What number is missing in the progression?")
    while right_ans <= 2:
        length = randint(5, 10)
        step = randint(-5, 5)
        first = randint(-10, 10)
        space = ''
        list = []
        count = 1
        while count <= length:
            list.append(first + (step * count))
            count += 1
        space = randint(0, length - 1)
        res = list[space]
        list[space] = ".."
        print(*list)
        ans = input()
        if str(res) == ans:
            right_ans += 1
            print('Correct!')
        else:
            print(str(ans) + ' is wrong answer ;(. '
                  'Correct answer was ' + str(res))
            print('Try again, ' + name + '.')
            return
    print('Congratulation, ' + name + "!")
    return
