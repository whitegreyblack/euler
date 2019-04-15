# problem 31
# coins sum
"""
In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
# analysis
"""
2 pound =>
  | 2 x 1 pound
  | 4 x 50 p
  | 10 * 20p
  | 20 * 10p
  | 40 * 5p
  | 100 * 2p
  | 200 * 1p
Dynamic programming
"""
results = [0 for _ in range(200)]
def combinations(x):
    yield x
for c in combinations(10):
    print(c)

