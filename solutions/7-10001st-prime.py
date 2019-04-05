# problem 7
# 10001st prime
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def find_nth_prime(x):
    i = 2
    primes = []
    while len(primes) < x:
        is_not_prime = False
        for j in range(2, (i//2)+1):
            if i % j == 0:
                is_not_prime = True 
                break
        if not is_not_prime:
            primes.append(i)
        i += 1
    return primes

# print(list(find_nth_prime(10001)))

# euler answer
from math import floor, log, sqrt
def is_prime(n):
    if n == 1:
        return False
    elif n < 4: # 2, 3
        return True
    elif n % 2 == 0:
        return False
    elif n < 9: # 5, 7
        return True
    elif n % 3 == 0: 
        return False
    else:
        r = floor(sqrt(n)) # sqrt(n) rounded to the greatest integer r so that r * r < n
        f = 5
        while f <= r:
            if n % f == 0 or n % (f + 2) == 0:
                return False
            f = f + 6
        return True

limit = 199
count = 1
candidate = 1
while count <= limit:
    candidate += 2
    if is_prime(candidate):
        count = count + 1
print(candidate)