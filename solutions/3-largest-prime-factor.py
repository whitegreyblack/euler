# problem 3
# largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Steps:
# find factors
# find pull primes
# find largest prime
number = 600851475143
# number = 13195
def factor(x:int=number):
    a = 1
    while a < x:
        yield a
        a += 1

def is_prime(x):
    if x < 3 or x % 2 == 0:
        return x == 2
    return not any(x % i == 0 for i in range(3, int(x ** 0.5 + 2), 2))


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

primes = set()
for i in range(2, number // 2 + 1):
    if number % i == 0:
        s = ""
        if is_prime(i):
            primes.add(i)
            s += str(i)
        divisor = number // i
        if is_prime(divisor):
            primes.add(divisor)
            s += " " + str(divisor)
        if s:
            print(s)

# primes = list(get_primes(number // 2 + 1))
print(max(primes))

