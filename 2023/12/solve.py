from algas.input import tokens
from algas.aoc.aoc import part1, part2
from functools import cache


@part2(lambda string: '?'.join([string]*5), lambda groups: ','.join([groups]*5))
@part1(lambda string: string, lambda groups: groups)
def solve2(pattern_modifier, group_modifier):
    @cache
    def solve(pattern, groups):
        solutions = 0
        if not pattern:
            return int(not groups)
        if not groups and pattern:
            return int(all('.' in c for c in pattern))
        if len(pattern) < groups[0]:
            return 0

        if '#' in pattern[0] and all('#' in c for c in pattern[:groups[0]]) and '.' in pattern[groups[0]]:
            solutions += solve(pattern[groups[0]+1:], groups[1:])
        if '.' in pattern[0]:
            solutions += solve(pattern[1:], groups)

        return solutions

    total = 0
    for pattern_string, groups_string in tokens():
        pattern = ('#.' if x == '?' else x for x in pattern_modifier(pattern_string) + '.')
        groups = (int(x) for x in group_modifier(groups_string).split(','))
        total += solve(tuple(pattern), tuple(groups))

    return total


#@part1(0)
def solve1(n):
    def str_to_patten(pattern_string):
        return tuple(len(x) for x in pattern_string.split('.') if len(x) > 0)

    for line in lines():
        pattern_string, groups_string = line.split()
        pattern = list(pattern_string)
        groups = tuple(int(x) for x in groups_string.split(','))
        wildcard_idx = [i for i, ltr in enumerate(pattern_string) if ltr == '?']

        for i in range(2**len(wildcard_idx)):
            cand = list(pattern)
            for j, idx in enumerate(wildcard_idx):
                cand[idx] = '#' if i & (1 << j) else '.'

            if str_to_patten(''.join(cand)) == groups:
                n += 1

    return n

if __name__ == '__main__':
    pass
