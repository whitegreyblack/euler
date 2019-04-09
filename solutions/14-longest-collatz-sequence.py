# problem 14
# Longest Collatz sequence
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
def collatz(x):
    if x == 1:
        return x
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1

def collatz_count(x):
    count = 0
    while x != 1:
        x = collatz(x)
        count += 1
    return count

number = 0
longest = 909
for x in range(979_999_999, 970_000_001, -2):
    count = collatz_count(x)
    if count > longest:
        longest = count
        number = x
        print(number, longest)
print(number, longest)
# 999_999_998 = 361
# 999_999_999 = 361
# 999_874_217 = 816
# 992_251_339 909