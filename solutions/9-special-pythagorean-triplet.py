# problem 9
# 9-special-pythagorean-triplet
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
# series of equations
a < b < c
a + b + c = 1000
a = 1000 - b - c

a**2 + b**2 = c**2
(1000 - b - c) ** 2 + b**2 = c**2
        1000     -b     -c
1000 1000000 -1000b -1000c
  -b  -1000b   b**2     bc
  -c  -1000c     bc   c**2

a**2 = 1000000 + b**2 + c**2 + 2bc - 2000b - 2000c
a**2 = b**2 + c**2 + 2bc - 2000b - 2000c + 1000000
b**2 + c**2 + 2bc - 2000b - 2000c + 1000000 + b**2 = c**2
---
min:
a = 0, b = 1, c = 32
max:
-- wrong logic. Sum is equal to 1000
31 < sqrt(1000) < 32 
-----
500 = c, b = 499, a = 1
250000 = 249001 + 1 | X
500 = c, b = 251, a = 249
250000 = 63001 + 62001 = 125002 | X | too little
500 = c, b = 400, a = 100
250000 = 160000 + 100000 = 170000 | X | too little

c = 400, b = 350, c = 250
160000 = 122500 + 62500
       = 185000
c = 400, b = 325, c = 275
160000 = 105625 + 75625 
       = 181250
c = 450, b = 350, c = 200
202500 = 122500 + 40000
       = 162500
c = 425, b = 375, a = 200
180625 = 140625 + 40000
       = 180625
"""
print(425 * 375 * 200)

# euler straightforward answer
s = 1000
for a in range(3, ((s-3) // 3) + 1):
    for b in range(a + 1, ((s - 1 - a) // 2) + 1):
        c = s - a - b
        if c**2 == a**2 + b**2:
            print("answer:", a, b, c)