from algas.input import lines
from algas.aoc.aoc import part1, part2
import re


@part2(['\d', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero'])
@part1(['\d'])
def main(extra_digits):
    d_map = {str(key): i % 10 for i, key in enumerate(list(range(1, 10)) + extra_digits)}
    total = 0
    for line in lines():
        digits = re.findall(rf'(?=({"|".join(extra_digits)}))', line)
        total += int(d_map[digits[0]]) * 10 + int(d_map[digits[-1]])
    return total


if __name__ == '__main__':
    pass
