from random import randint


def gcd(name):
    i = 0
    while i <= 2:
        a = randint(1, 100)
        b = randint(1, 100)
        print('Find the greatest common divisor of given numbers.')
        print(f"Question: {a} {b}")
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
            print('Let\'s try again, ' + name + "!")
            return
    print('Congratulations, ' + name + '!')
    return
