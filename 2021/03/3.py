import sys
sys.path.append('C:/Users/oscar/Code/Bnanan/Python/algas/src')
from algas.lists import top_n, group
from algas.input import lines
from aoc.aoc import part1and2

@part1and2()
def main():
    counts = [0] * 12
    a = 0
    b = 0
    lin = list(lines())
    for value in lin:
        for i, x in enumerate(value):
            counts[i] += int(x)
    for i, n in enumerate(counts[::-1]):
        if n > len(lin) // 2:
            a += 1 << i
        else:
            b += 1 << i

    return a * b,
