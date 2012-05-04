from math import sqrt


def is_prime(number):
    '''
    Check whether the number is prime.

    Keywortd arguments:
    number -- the number who will be checked

    Return: bool
    '''
    return all([number % divisor for divisor
        in range(2, int(sqrt(number)) + 1)])


def primes():
    '''
    Generator for a prime numbers.
    '''
    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1


def prime_divisors(number):
    '''
    Gets all prime divisors of the number.

    Keywortd arguments:
    number -- the number whose prime divisors will be searched

    Return: list
    '''
    divisors = []
    for prime in primes():
        while number % prime == 0:
            divisors.append(prime)
            number /= prime
        if number == 1:
            return divisors


def semiprimes():
    '''
    Generator for a semiprime numbers.
    (semi-primes - numbers with exacly 2 prime divisors)
    '''
    number = 4
    while True:
        if len(prime_divisors(number)) == 2:
            yield number
        number += 1
