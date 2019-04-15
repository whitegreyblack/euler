# problem C
# coin jam
import math as m
from functools import lru_cache
# precompute primes

@lru_cache(maxsize=None)
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

def is_prime2(n):
    if n < 3 or n % 2 == 0:
        return n == 2
    return not any(n % i == 0 for i in range(3, int(n ** 0.5 + 2), 2))

def is_jamcoin(x):
    return int(x[0]) == 1 and int(x[-1]) == 1

def find_factor(x):
    for factor in range(3, (x // 2) + 1):
        if x % factor == 0:
            return factor

def find_factor2(x):
    i = 1
    while i * i <= x:
        if x % i == 0:
            return factor
        elif x / i != i:
            return x / i
        i += 1
    return x

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
            # converts to str to remove leading '0b'
            bin_str = strip_bin(num_bin) 
            if not is_jamcoin(bin_str):
                continue
            base_nums = []
            has_prime = False
            for base in range(2, 11):
                # convert_base takes in a string as input
                base_num = convert_base(bin_str, base) 
                if is_prime2(base_num):
                    has_prime = True
                    break
                base_nums.append(base_num)
            if not has_prime:
                print(bin_str)
                bit_values.append((bin_str, base_nums))
        """
        output.append(f"Case #{case_num}:")
        for bit_value, base_values in bit_values:
            values = ' '.join(str(find_factor2(b)) for b in base_values)
            out = f"{bit_value} {values}"
            print(len(output), out)
            output.append(out)
        """
    print('\n'.join(output))
