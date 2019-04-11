# problem 22
# Names score
"""
Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def parse(path):
    with open(path, 'r') as f:
        lines = f.read()
    return lines.split(',')
def format(names):
    return [name.replace('"', '') for name in names]
def score(name):
    return sum(ord(letter) - 96 for letter in name.lower())

names = [(i+1, n) for i, n in enumerate(sorted(format(parse('./names.txt'))))]
print(names[937])
scores_sum = 0
for i, n in names:
    scores_sum += i * score(n)
print(scores_sum)
