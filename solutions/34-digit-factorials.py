# problem 34
# digit factorials
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of 
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
cache = {}
def factorial(x):
    if x < 1:
        return 1
    f = cache.get(x, None)
    if f:
        return f
    cache[x] = x * factorial(x-1)
    return cache[x]
def sum_factorial(x):
    factorials = [factorial(int(i)) for i in str(x)]
    sum_facts = sum(factorials)
    return sum_facts
# print(factorial(5))
# print(cache.items())
# print(factorial(4))
for i in range(3, 99_999_999):
    if sum_factorial(i) == i:
        print(i)

