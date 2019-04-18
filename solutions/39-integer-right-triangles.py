# problem 39
# integer right triangles

"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are
exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?

------
Equations:
    a + b + c = p
    a^2 + b^2 = c^2
System of Equations:
    c = p - a - b
    a^2 + b^2 = (p-a-b)^2
        p   -a   -b
      p p^2 -pa  -pb
     -a -pa  a^2  ab
     -b -pb  ab   b^2
              = p^2 - 2pa - 2pb + a^2 + 2ab + b^2
              = p^2 - 2p(a + b) + (a + b)^2
            0 = p^2 - 2p(a + b) + 2ab
          p^2 = 2p(a+b) - 2ab
        p^2/2 = p(a+b) - ab
        p^2/2 = pa + pb - ab
"""

from collections import defaultdict
from functools import reduce
import operator as op

cache = {}
def fib(x):
    if x in cache:
        return cache[x]
    cache[x] = 1 if x < 2 else fib(x-1) + fib(x - 2)
    return cache[x]

def gen_nums(i, j):
    a, b = i, j
    c = a + b
    d = b + c
    return a, b, c, d

def naive():
    combs = set()
    p = defaultdict(int)
    i = 1
    outer_break = False

    while i < 1000:
        j = i
        while j < 1000:
            nums = gen_nums(i, j)
            m = 1
            s = 0
            while s <= 1000:
                a = nums[0] * nums[3] * m
                b = nums[1] * nums[2] * 2 * m
                c = (nums[1] ** 2 + nums[2] ** 2) * m
                if a ** 2 + b ** 2 != c ** 2:
                    continue
                s = a + b + c
                if s <= 1000:
                    nums_str = '[' + ' '.join(str(x) for x in nums) + ']'
                    combs.add((i, j, nums_str, m, a, b, c, s))
                    p[s] += 1
                    m += 1
            j += 1
        i += 1

    variables = 'i j nums m a b c p'.split()
    print('\n'.join(', '.join(f'{k}:{v}' for k, v in zip(variables, i)) for i in combs))
    def bucket_sort(p):
        q = defaultdict(list)
        for k, v in p.items():
            q[v].append(k)
        return sorted([(k, v) for k, v in q.items()], key = lambda x: x[-2])
    for k, v in bucket_sort(p):
        print(k, v)

def solution(n):
    max_n, max_p = 0, None
    for p in range(2, n+1, 2):
        c = 0
        for a in range(2, p // 3):
            if p * (p - 2 * a ) % (2 * (p - a)) == 0:
                c += 1
        if c > max_n:
            max_n = c
            max_p = p
    return max_p
print(solution(1000))

sols = [0 for _ in range(1001)]

for x in range(1, 500):
    for y in range(x,501-x):
        z = (x**2+y**2)**0.5
        if z-int(z)==0:
            sols[int(x+y+z)]+=1

print(sols.index(max(sols)))
