# problem 30
# digit fifth powers
"""
Surprisingly there are only three numbers that can be written as the 
sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum 
of fifth powers of their digits.
"""
sum_power_of = lambda l, p: sum(d**p for d in l)
split_digit = lambda n: [int(x) for x in str(n)]
def digit_powers(number, power=5):
    digits = split_digit(number)
    s = sum_power_of(digits, power)
    return s == number

s = 0
for i in range(2, 1_000_000):
    if digit_powers(i):
        s += i
print(s)
