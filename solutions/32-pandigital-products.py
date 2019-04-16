# problem 32
# pandigital products
"""
We shall say that an n-digit number is pandigital if it makes use of all their 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can 
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.

# analyis
find range of x * y = z where len(x + y + z) == 9
100(3) *  100(3) = 10000(5) -! 10 invalid
 99(2) *  999(3) = 98901(5) -! 10 invalid
 50(2) *  999(3) = 49950(5) -! 10 invalid
 10(2) *  100(3) =  1000(4) -!  9 valid
  1(1) * 1000(4) =  9000(4) -!  9 valid
  1(1) * 9999(4) =  9999(4) -!  9 valid lower = 1, upper = 9999
  2(2) * 5000(4) = 10000(5) -! 10 invalid
  2(2) * 4999(4) =  9998(4) -!  9 valid
 39(2) *  186(3) =  7524(4) -!  9 valid
 20(2) *  200(3) = 40
"""

def pandigital_product(x, y, z):
    digits = [False for _ in range(len(str(x) + str(y) + str(z)))]
    for number in (x, y, z):
        for digit in str(number):
            if digits[int(digit) - 1] == True:
                return False
            digits[int(digit) - 1] = True
    return all(digits)

def pandigital(x):
    digits = [False for _ in range(len(str(x)))]
    for digit in list(str(x)):
        # we saw the number again -- exit early
        if digits[int(digit)-1] == True:
            return False
        digits[int(digit)-1] = True
    return all(digits)
pairs = set()
sums = []
for i in range(1, 10000):
    if '0' in list(str(i)):
        continue
    for j in range(1000 // i, 9999 // i + 1):
        if '0' in list(str(j)):
            continue
        if set([i, j]) in pairs:
            continue
        product = i * j
        if '0' in list(str(product)):
            continue
        """
        smaller_than_i = len(str(product)) < len(str(i))
        smaller_than_j = len(str(product)) < len(str(j))
        if smaller_than_i or smaller_than_j:
            break
        """
        if len(str(i)) + len(str(j)) + len(str(product)) == 9:
            if pandigital_product(i, j, product):
                print(i, j, product)
                pairs.add((i, j))

                sums.append(product)
print(sum(sums))
# print(pandigital(15234))
# print(pandigital(155234))
    
