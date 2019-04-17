# problem 38
# pandigital multiples
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will 
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 
and 5, giving the pandigital, 918273645, which is the concatenated product of 
9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ... , n) where n > 1?

Smallest x = 1, n = 9
Largest x = 987654321, n = 1 ! not valid
Second largest x = 999_999_999 // 398_765_421
"""
def is_pandigital(x):
    return set(x) == set('123456789')
def is_concatenated_product_pandigital(x):
    products = []
    n = 1
    break_loop = False
    while not break_loop:
        s = ''
        for i in range(1, n+1):
            s += str(x * i)
            if len(s) > 9:
                break_loop = True
                break
        if len(s) < 9:
            i += 1
            continue
        if is_pandigital(s):
            products = (x, i, int(s))
def check_concatenated_product_pandigital(x, n):
    s = ''
    for i in range(1, n+1):
        s += str(x * i)
    return s
def find_cpp(x):
    products = []
    n = 1
    loop_should_continue = True
    while loop_should_continue:
        s = ''
        for i in range(1, n+1):
            s += str(x * i)
        if len(s) > 9:
            loop_should_continue = False
        elif len(s) == 9:
            p = is_pandigital(s)
            if p:
                products.append((x, i, int(s), p))
            loop_should_continue = False
        n += 1
    return products
products = []
limit = 398_765_421
# limit = 192
for i in range(1, limit+1):
    print(i)
    p = find_cpp(i)
    if p:
        products += p
print(products[0])
for i in sorted(products, key=lambda x: x[2]):
    print(i)
"""
x = 9
n = 5
s = check_concatenated_product_pandigital(x, n)
p = is_pandigital(s)
print(x, n, s, p)
x, n = 192, 3
s = check_concatenated_product_pandigital(x, n)
p = is_pandigital(s)
print(x, n, s, p)
"""
# print(is_concatenated_product_pandigital(9))
