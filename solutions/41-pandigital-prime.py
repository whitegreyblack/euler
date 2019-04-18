# problem 41
# pandigital prime
"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
also prime.

What is the largest n-digit pandigital prime that exists?
"""
from lib import primes_under, is_pandigital
:w
for x in primes_under(100_000_000):
    if is_pandigital(x):
        print(x)

