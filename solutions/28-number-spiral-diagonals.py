# problem 28
# Number spiral diagonals
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

[21]22 23 24[25]
 20 [7] 8 [9]10
 19  6 [1] 2 11
 18 [5] 4 [3]12
[17]16 15 14[13]

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

3 1 + 3 + 5 + 7 + 9 + 13 + 17 + 21 + 25 = 101
"""
import math
# f = lambda x: 2 * math.ceil(x // 4) + 1
ranges = lambda x: ((2*x-1)**2 + 1, (2*x+1)**2)
jumps = lambda x: ((2*x-1)**2 + (2*x), (2*x+1)**2)
j = lambda x, y: ((2*x-1)**2 + (2*x)) + 2 * x * y
"""
0 | 1 | 1  -> 1   | 0**2 + 1 -> 1**2 |  1  1  1  1 | diff 0 = 2 * 0
1 | 2 | 2  -> 9   | 1**2 + 1 -> 3**2 |  3  5  7  9 | diff 2 = 2 * 1
2 | 3 | 10 -> 25  | 3**2 + 1 -> 5**2 | 13 17 21 25 | diff 4 = 2 * 2
3 | 4 | 26 -> 49  | 5**2 + 1 -> 7**2 | 31 37 43 49 | diff 6 = 2 * 3
4 | 5 | 50 -> 81  | 7**2 + 1 -> 9**2 |             | diff 8 = 2 * 4
                    (2*i-1)**2
"""
x = 501
s = set()
for x in range(x):
    for y in range(4):
        s.add(j(x, y))
print(max(s))
print(sum(s))
print(math.sqrt(1001))