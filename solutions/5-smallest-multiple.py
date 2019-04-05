# problem 5
# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?

from functools import reduce # Valid in Python 2.6+, required in Python 3
from math import log, floor, sqrt
import operator as op
number = 20

def check_divisible_by(x, r):
    for i in range(1, r+1):
        if x % i:
            return False
    return True

def smallest_multiple(jump):
    mul = reduce(op.mul, list(i+1 for i in range(jump)))
    for i in range(jump, mul, jump):
        if check_divisible_by(i, r=jump):
            return i
# print(smallest_multiple(number))

# euler answer
def create_primes(x):
    # total = 0
    for i in range(1, x+1):
        count = 0
        for j in range(2, (i//2)+1):
            if i % j == 0:
                count += 1
                break
        if count == 0 and i != 1:
            # total = total + i
            yield i
    # yield total

def smallest_multiple_quick(k):
    N = 1
    i = 1
    check = True
    limit = sqrt(k)
    primes = list(create_primes(k))
    a = dict()

    for p in primes:
        a[i] = 1
        if check:
            if p <= limit:
                a[i] = floor(log(k) / log(p))
            else:
                check = False
        N *= p ** a[i]
        i += 1
    return N

print(smallest_multiple_quick(number))