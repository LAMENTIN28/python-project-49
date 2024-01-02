from random import randint


def prime(name):
    ind = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while ind <= 2:
        i = 2
        count = 0
        num = randint(1, 1000)
        print(num)
        while i < num:
            if num % i == 0:
                count += 1
            i += 1
        if count == 0:
            ans = "yes"
        else:
            ans = "no"
        ans_u = input()
        if ans == ans_u:
            print('Correct!')
            ind += 1
        else:
            print(str(ans_u) + ' is wrong answer ;(. '
                  'Correct answer was ' + str(ans))
            return
    print('Congratulation, ' + name + "!")
    return
