# problem 20
# Factorial digit sum
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import functools as fn
import operator as op
x = 100
product_sum = fn.reduce(op.mul, range(1, x+1), 1)
digit_sum = sum(int(i) for i in str(product_sum))
print(digit_sum)
