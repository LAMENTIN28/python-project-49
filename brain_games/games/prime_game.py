from random import randint


def prime_count():
    i = 2
    count = 0
    number = randint(1, 1000)
    exclam = f"{number}"
    right_ans = 'yes'
    while i < number:
        if number % i == 0:
            count += 1
            right_ans = "no"
        i += 1
    return [right_ans, exclam]


def prime(name, func):
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    func(prime_count, name, question)
    return
