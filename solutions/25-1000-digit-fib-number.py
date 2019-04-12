# 25
# 1000-digit Fibonacci number
"""
The Fibonacci sequence is defined by the recurrence relation:

F(n) = F(n−1) + F(n−2), where F(1) = 1 and F(2) = 1.
Hence the first 12 terms will be:

F(1)= 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
F(10) = 55
F(11) = 89
F(12) = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
cache = {}
def fib(x):
    if x in cache:
        return cache[x]
    if x == 1:
        cache[x] = 1
        return 1
    if x == 2:
        cache[x] = 2
        return 2
    cache[x] = fib(x-1) + fib(x-2)
    return cache[x]
x = 0
f = 12
while len(str(x)) < 1_000:
     f += 1
     x = fib(f)
print(f, len(str(x)))
print(f, len(str(fib(f))), f-1, len(str(fib(f-1))))