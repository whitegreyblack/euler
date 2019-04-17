# problem 14
# Longest Collatz sequence
"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n ->3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
cache = {}
def collatz(x):
    if x in cache:
        return cache[x]

    if x == 1:
        cache[x] == x
    elif x % 2 == 0:
        cache[x] = x // 2
    else:
        cache[x] = 3 * x + 1
    return cache[x]

def collatz_count(x):
    count = 0
    while x != 1:
        x = collatz(x)
        count += 1
    return count

number = 0
longest = 0

for x in range(1, 1_000_001):
    count = collatz_count(x)
    print(x, count)
    if count > longest:
        longest = count
        number = x
print(number, longest)
# 999_999_998 = 361
# 999_999_999 = 361
# 999_874_217 = 816
# 992_251_339 909
