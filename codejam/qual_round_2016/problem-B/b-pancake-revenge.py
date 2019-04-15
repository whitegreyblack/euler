# problem B
# Revenge of the Pancakes
happy = '+'
blank = '-'
def transform(string):
    return [bool(s == '+') for s in string]
def format_output(case_num, flips):
    return f"Case #{case_num}: {flips}"
def flip(case):
    stack = list(case)
    state = stack[0]
    next_state = happy if stack[0] == '-' else blank
    i = 1
    while i < len(stack) and stack[i] == state:
        i += 1
    for i in range(i):
        stack[i] = next_state
    return ''.join(stack)

cases = int(input())
output = [None for _ in range(cases)]
for case_index in range(1, cases+1):
    case = input()
    t = transform(case)
    if all(t):
        output[case_index-1] = format_output(case_index, 0)
        continue
    flips = 0
    while not all(t):
        case = flip(case)
        flips += 1
        t = transform(case)
    output[case_index-1] = format_output(case_index, flips)
print('\n'.join(output))


