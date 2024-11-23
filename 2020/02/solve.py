from aoc.input import tokens_pattern
from aoc.aoc import part1and2


@part1and2()
def solve():
    valids1 = 0
    valids2 = 0
    for low, high, char, password in tokens_pattern(regex=r'(\d+)-(\d+) (.): (.+)'):
        low = int(low)
        high = int(high)
        count = 0
        for c in password:
            count += int(c == char)
        valids1 += int(low <= count <= high)
        valids2 += int((password[low-1] == char) ^ (password[high-1] == char))
    return valids1, valids2

if __name__ == '__main__':
    pass
