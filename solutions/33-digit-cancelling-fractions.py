# problem 33
# digit cancelling fractions
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which 
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less 
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.
"""
fractions = []
for i in range(10, 100):
    for j in range(10, 100):
        si = str(i)
        sj = str(j)
        if si[1] == sj[0] and int(si[0]) != 0 and int(sj[1]) != 0:
            if i / j == int(si[0]) / int(sj[1]):
                print(i, j, si[0], sj[1], i / j, int(si[0]) / int(sj[1]))
            # fractions.append((i, j))  
for n, d in fractions:
    print(f'{n}/{d}')
f = [
  (49, 98, 0.5),
  (26, 65, 0.4),
  (16, 64, 0.25),
  (19, 95, 0.2),
]
xp, yp = 1, 1
for (x, y, _) in f:
    xp *= x
    yp *= y
print(yp // xp)

