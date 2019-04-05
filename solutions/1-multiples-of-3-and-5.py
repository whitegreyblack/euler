# problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Simple:
print(sum(i for i in range(1000) if not (i % 3) or not (i % 5)))

# Complex:
sumBy = lambda x, t: x * (t//x * ((t//x)+1)) // 2
print(sumBy(3, 999) + sumBy(5, 999) - sumBy(15, 999))
