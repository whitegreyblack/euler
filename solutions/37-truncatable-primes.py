# problem 37
# truncatable primes
"""
The number 3797 has an interesting property. Being prime itself, it is 
possible to continuously remove digits from left to right, and remain prime 
at each stage: 
    3797, 797, 97, and 7. 
Similarly we can work from right to left: 
    3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

3 37 379 3797 797 97 7
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
def is_truncatable_prime(x):
    if x < 10:
        return False
    # go right to left
    right_to_left = x
    while right_to_left > 9:
        right_to_left //= 10
        if right_to_left not in primes:
            return False
    left_to_right = x
    while left_to_right > 9:
        left_to_right %= 10 ** (len(str(left_to_right)) - 1)
        if left_to_right not in primes:
            return False
    return True
s = 0
x = 1_000_000
primes = set(get_primes(x))
for i in primes:
    if is_truncatable_prime(i):
        s += i
print(s)

