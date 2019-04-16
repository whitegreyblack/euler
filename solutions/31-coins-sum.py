# problem 31
# coins sum
"""
In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
    1 x £1 +  x 50p + 2 x 0p + 1 x 5p + 1 x 2p + 3 x 1p
How many different ways can £2 be made using any number of coins?
"""
def count(S, n):
    m = len(S)
    table = [[ 0 for _ in range(m)] for _ in range(n + 1)]
    for i in range(m):
        table[0][i] = 1
    for i in range(1, n+1):
        for j in range(m):
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y
    return table[n][m-1]

# time complexity m * n but above uses space (m * n) below uses space (n)

def count2(S, n):
    m = len(S)
    table = [0 for _ in range(n + 1)]
    table[0] = 1
    print('i j t[j] t[j-S[i]]')
    for i in range(m): # iterate through the numbers list
        print(f'Using number {i}/{S[i]}')
        for j in range(S[i], n+1):
            print(f'{i} {j} Adding {table[j - S[i]]} to {table[j]}')
            table[j] += table[j - S[i]]
        print(f'Table is now {table}')
    return table[n]
"""
S = 1, 2, 3
base = [1, 0, 0, 0, 0] # len(n+1), n=4, len(base) = 5
for i in range(3):
    for j in range((1, 4), (2, 4), (3, 4)):
        pass     
"""
arr = [1, 2, 3]
n = 2
print(count2(arr, n))

arr = [1, 2, 5, 10, 20, 50, 100, 200]
n = 200
# print(count2(arr, len(arr), n))

