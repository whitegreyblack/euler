# problem 35
# circular primes
"""
The number, 197, is called a circular prime because all rotations of the 
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 
73, 79, and 97.

How many circular primes are there below one million?
"""
cache = {}
def is_circular_prime(x):
    # single digits are always circular primes
    if x < 10:
        return True
    str_x = list(str(x))
    for i in range(len(str_x)):
        head = str_x.pop(0)
        str_x.append(head)
        if not is_prime(int(''.join(str_x))):
            return False
    return True

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
count = 0
for p in get_primes(1_000_000):
    if is_circular_prime(p):
        count += 1
        print(p)
print(count)
