from random import randint


def gcd(name):
    i = 0
    while i <= 2:
        a = randint(1, 100)
        b = randint(1, 100)
        print(a, b)
        e = 1
        while e <= a and e <= b:
            if a % e == 0 and b % e == 0:
                ans = e
            e += 1
        ansu = input()
        if str(ans) == ansu:
            print('Correct!')
            i += 1
        else:
            print(str(ansu) + ' is wrong answer ;(. '
                  'Correct answer was ' + str(ans))
            print('Try again, ' + name + '.')
            return
    print('Congratulation, ' + name + '!')
    return
