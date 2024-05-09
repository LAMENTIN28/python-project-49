from random import randint


DEFINITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_answer_question():
    number = randint(1, 1000)
    answer = is_prime(number)
    answer = 'yes' if is_prime(number) is True else 'no'
    return answer, str(number)


def is_prime(number):
    i = 2
    while i < number:
        answer = False if abs(number) % i == 0 else True
        if answer is False:
            return answer
        i += 1
    return answer
