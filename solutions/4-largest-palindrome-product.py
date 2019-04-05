# Problem 4
# Largest palindrome product
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is:
#   9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(x):
    str_x = str(x)
    even = 0 if len(str_x) % 2 == 0 else 1
    l = len(str_x) // 2
    left = str_x[:l]
    right = str_x[l+even:]
    return int(left) == int(right[::-1])


def find_palindromes():
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if is_palindrome(i * j):
                yield i, j, i * j

def find_palindromes_quick():
    largest = 0
    a = 999
    while a > 99:
        factor11 = a % 11 == 0
        b = 999 if factor11 else 990
        db = 1 if factor11 else 11
        while b >= a:
            v = a * b
            if v <= largest:
                break
            if is_palindrome(v):
                largest = v
            b -= db
        a = a-1
    return largest

# largest, *_ = sorted(find_palindromes(), key=lambda x: x[2], reverse=True)
# print(largest)
print(find_palindromes_quick())
# print(is_palindrome(90009))
# print(is_palindrome(9009))