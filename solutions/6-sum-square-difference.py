# problem 6
# Sum square difference
"""
The sum of the squares of the first ten natural numbers is,
        1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

square = lambda x: x**2

def natural_numbers(x):
    for i in range(1, x+1):
        yield i

def square_numbers(x):
    for i in range(1, x+1):
        yield square(i)

def difference_square_natural(x):
    natural_sum = sum(map(square, natural_numbers(x)))
    square_sum = square(sum(natural_numbers(x)))
    return square_sum - natural_sum
print(difference_square_natural(100))

# Euler solution
limit = 100
natural_sum = (limit * (limit + 1)) // 2
square_sum = ((2 * limit + 1) * (limit + 1) * limit) // 6
print(natural_sum ** 2 - square_sum)