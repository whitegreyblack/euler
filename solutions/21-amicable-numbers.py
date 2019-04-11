# problem 21
# Amicable numbers
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
# -- Naive solution
# -- functions
def divisors(x):
    factors = []
    for i in range(1, x//2+1):
        if x % i == 0:
            factors.append(i)
    return factors
def divisors_sum(d):
    return sum(x for x in d)
def proper_divisors(x):
    if x in cache.keys():
        return cache[x]
    d = divisors_sum(divisors(x))
    dd = divisors_sum(divisors(d))
    cache[x] = x != d and x == dd
    if cache[x]:
        print(x, d, dd)
    return cache[x]
# cache = {}
pd = []
for i in range(1, 10_000):
    if proper_divisors(i):
        pd.append(i)
print(pd, sum(pd))

# -- efficient solution
def divsum(n):
    return sum(d+(n//d) for d in range(2+(n%2), int(n**(.5)), 1+(n%2)) if not n%d)+(n>1)

def amicable(maxim):
    divs = {n:divsum(n) for n in range(maxim)}
    return sum(n for n, d in divs.items() if n != d and divs.get(d,-1) == n)

for d in range(2 + (10_000 % 2), int(10_000 ** (.5)), 1 + (10_000 % 2)):
    if not 10_000 % d:
        print(d, d + (10_000 // d) + (10_000 > 1))

if __name__ == "__main__":
    print(amicable(10000))