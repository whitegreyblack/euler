# problem 36
# double-base palindromes
"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)
"""
def dec_to_bin(x):
    return bin(x).replace('0b', '')
def is_palindrome(x):
    str_num = str(x)
    mid = len(str_num) // 2
    left = str_num[:mid]
    right = str_num[len(str_num):mid-1:-1]
    return all(i == j for i, j in zip(left, right))
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def naive():
    dec_nums = []
    for dec_num in range(1, 1_000_000):
        # make sure dec num is palindrome
        # if not pali then continue
        if is_palindrome(dec_num):
            bin_num = dec_to_bin(dec_num)
            if is_palindrome(bin_num):
                dec_nums.append(dec_num)
    print(sum(dec_nums))
naive()
