# problem 41
# pandigital prime
"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
also prime.

What is the largest n-digit pandigital prime that exists?
"""
def is_pandigital(x):
    x = str(x)
    l = len(x) == len(set(x)) # make sure the no duplicates exist
    p = set(x) == set(''.join(str(i) for i in range(1, len(x)+1)))
    return l and p
print(is_pandigital(123))
print(is_pandigital(1123))
