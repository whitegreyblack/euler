# problem 10
# summation of primes
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
def get_primes(x):
    primes = [True for i in range(x + 1)]
    p = 2
    while p * p <= x:
        if primes[p] == True:
            for i in range(p * 2, x + 1, p):
                primes[i] = False
        p += 1
    for i in range(2, x):
        if primes[i]:
            yield i

print(sum(get_primes(2_000_000))) 

