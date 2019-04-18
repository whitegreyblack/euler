# lib.py
# holds stuff like factors, primes, and pandigital


from functools import reduce
import operator as op
from collections import defaultdict


def is_pandigital(x: int) -> bool:
    x = str(x)
    l = len(x) == len(set(x))
    p = set(x) == set(''.join(str(i) for i in range(1, len(x) + 1)))
    return l and p


def is_factor(number: int, factor: int) -> bool:
    return number % factor == 0


def factors_of(x: int) -> int:
    divisors = []
    for i in range(1, int(x ** 0.5 + 1)):
        if is_factor(x, i):
            divisors.append([i, x // i])
    for divisor in sorted(set(fn.reduce(list.__add__, divisors))):
        yield i


def is_prime(x: int) -> bool:
    if x < 3 or x % 2 == 0:
        return x == 2
    for i in range(3, int(x ** 0.5 + 2), 2):
        if is_factor(x, i):
            return False
    return True


def primes_from(x: int, start=2):
    pass

def primes_under(x: int) -> int:
    primes = [True for _ in range(x + 1)]
    p = 2
    while p * p <= x:
        if primes[p] == True:
            for i in range(p * 2, x + 1, p):
                primes[i] = False
        p += 1
    for i in range(2, x):
        if primes[i]:
            yield i


if __name__ == "__main__":
    def out(fn, args):
        name = fn.__name__
        if isinstance(args[0], (list, tuple)):
            results = '\n'.join(f'{name}({", ".join(f"{a}" for a in arg)}) = {fn(*arg)}' for arg in args)
        else:
            results = '\n'.join(f'{name}({arg}) = {fn(arg)}' for arg in args)
        print(results)

    out(is_pandigital, (123, 1123))
    out(is_factor, ((10, 2), (10, 3), (10, 5)))
    out(is_prime, (3, 5, 7, 9, 11))
    out(factors_of, (5, 10))

