# problem C
# coin jam
import math as m
# precompute primes
def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = m.floor(m.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0 or n % (f + 2) == 0:
                return False
            f = f + 6
        return True

def find_factor(x):
    for factor in range(3, (x // 2) + 1):
        if x % factor == 0:
            return factor

def bit_range(l):
    return 1 << int(l) - 1, 1 << int(l)

def strip_bin(b):
    return str(b).replace('0b', '')

def convert_base(number, base):
    return int(number, base=base)

if __name__ == "__main__":
    output = []
    cases = int(input())
    for case_num in range(1, cases+1):
        n, j = (int(x) for x in input().split(' '))
        bit_values = []
        for num in range(*bit_range(n)):
            if len(bit_values) >= j:
                break
            # convert num to binary then to base 2-10
            num_bin = bin(num)
            bin_str = strip_bin(num_bin) # converts to str to remove leading '0b'
            has_prime = False
            base_nums = []
            for base in range(2, 11):
                base_num = convert_base(bin_str, base) # convert_base takes in a string as input
                if is_prime(base_num):
                    has_prime = not has_prime
                    break
                base_nums.append(base_num)
            if not has_prime:
                bit_values.append((bin_str, base_nums))
        output.append(f"Case #{case_num}:")
        for bit_value, base_values in bit_values:
            values = ' '.join(str(find_factor(b)) for b in base_values)
            output.append(f"{bit_value} {values}")
    print('\n'.join(output))
