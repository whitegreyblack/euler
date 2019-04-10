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
import click

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
}

# add hundreds and thousands
for i in range(1, 10):
    num_words[i*100] = f'{num_words.get(i)} hundred'
    num_words[i*1000] = f'{num_words.get(i)} thousand'

def convert_number_to_words(x:int) -> str:
    words = num_words.get(x, [])
    if words:
        return words
    # at this point we should be x > 20
    nums = []
    factor = 1
    while x > 0:
        modded = x % 10
        placement = modded * factor
        if placement:
            nums.insert(0, placement)
        x //= 10
        factor *= 10
    needs_add = False
    and_added = False
    teens = False
    tens = False
    # goes from large to big
    for v in nums:
        if v == 0:
            continue
        if v > 99:
            needs_add = True
        # handle 11 -> 19
        if v == 10:
            teens = True
        elif v < 10 and teens:
            v += 10
            teens = not teens

        # handle 20, 30, 40, ..., 90
        # if 2 < v // 10 < 10:
        #     tens = True
        # elif v < 10 and tens:
        #     words.append('-')
        #     tens = not tens

        if not teens:
            words.append(num_words.get(v, None))
        if needs_add and not and_added:
            words.append('and')
            and_added = not and_added
            needs_add = not needs_add
    return ' '.join(words)

def convert_words_to_count(s:str) -> int:
    return len(s.replace(' ', ''))

@click.command()
@click.argument('number', nargs=1)
def main(number):
    count = 0
    for i in range(1, int(number) + 1):
        number_word = convert_number_to_words(i)
        letter_count = convert_words_to_count(number_word) 
        print(number_word, letter_count)
        count += letter_count
    print(count)

if __name__ == '__main__':
    main()