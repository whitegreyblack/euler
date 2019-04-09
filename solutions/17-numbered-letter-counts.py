# problem 17
# number letter counts
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""
from math import floor

num_words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred"
}

def convert_number_to_words(x:int) -> str:
    words = num_words.get(x)
    if words:
        return words
    # at this point we should be x > 20
    nums = []
    while x > 99:
        modded = x % 10
        x //= 10
        nums.insert(0, modded)
    nums.insert(0, x)
    words_list = []
    for i, v in enumerate(nums):
        if 20 < x < 100:
            tens = int(floor(x//10)*10)
            ones = x % 10
        print(i, v)
    return nums

def convert_words_to_count(s:str) -> int:
    pass

for i in range(100, 104):
    print(convert_number_to_words(i))