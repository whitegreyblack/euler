# problem 3
# largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Steps:
# find factors
# find pull primes
# find largest prime
number = 600851475143
number = 13195
def factor(x:int=number):
    a = 1
    while a < x:
        yield a
        a += 1

print(factor())