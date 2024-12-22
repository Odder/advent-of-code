from functools import cache
from itertools import pairwise, permutations, product
from algs.spaces.imaginary_s2 import load_grid
from aoc.input import lines, grouped_lines, tokens_pattern
from aoc.aoc import part1, part2, part1and2, part1and2yield
from algs.search import BFS, DFS, PFS


keypad = load_grid([
    ' ^A',
    '<v>',
])
paths = {
    ('A','^'): ['<A'],
    ('A','<'): ['v<<A', '<v<A', '<<vA'],
    ('A','v'): ['v<A', '<vA'],
    ('A','>'): 'vA',
    ('A','A'): 'A',
    ('^', '^'): 'A',
    ('^', '<'): 'v<A',
    ('^', 'v'): 'vA',
    ('^', '>'): 'v>A',
    ('^', 'A'): '>A',
    ('<', '^'): '>^A',
    ('<', '<'): 'A',
    ('<', 'v'): '>A',
    ('<', '>'): '>>A',
    ('<', 'A'): '>>^A',
    ('v', '^'): '^A',
    ('v', '<'): '<A',
    ('v', 'v'): 'A',
    ('v', '>'): '>A',
    ('v', 'A'): '>^A',
    ('>', '^'): '^<A',
    ('>', '<'): '<<A',
    ('>', 'v'): '<A',
    ('>', '>'): 'A',
    ('>', 'A'): '^A',
}
paths = {
    ('A','^'): ['<A'],
    ('A','<'): ['v<<A', '<v<A'],
    ('A','v'): ['v<A', '<vA'],
    ('A','>'): ['vA'],
    ('A','A'): ['A'],
    ('^', '^'): ['A'],
    ('^', '<'): ['v<A'],
    ('^', 'v'): ['vA'],
    ('^', '>'): ['v>A', '>vA'],
    ('^', 'A'): ['>A'],
    ('<', '^'): ['>^A'],
    ('<', '<'): ['A'],
    ('<', 'v'): ['>A'],
    ('<', '>'): ['>>A'],
    ('<', 'A'): ['>>^A', '>^>A'],
    ('v', '^'): ['^A'],
    ('v', '<'): ['<A'],
    ('v', 'v'): ['A'],
    ('v', '>'): ['>A'],
    ('v', 'A'): ['^>A', '>^A'],
    ('>', '^'): ['^<A', '<^A'],
    ('>', '<'): ['<<A'],
    ('>', 'v'): ['<A'],
    ('>', '>'): ['A'],
    ('>', 'A'): ['^A'],
}

@cache
def min_length(s, rounds=2, start=False):
    length = 0
    print('ml', s, rounds)
    s = 'A' + s if start else s
    for f, t in pairwise(s):
        if rounds == 0:
            print('at the end, looking up', f, t)
            length += len(paths[(f, t)])
        else:
            print('in the midst, looking up', f, t)
            length += min(min_length(x, rounds-1, start) for x in paths[(f, t)])
        start = False
    print('return', s, length, rounds)
    return length or 1




@part1()
def solve1(ans=0):
    #generate all combinations of <^>v between the A's
    for k, initial in [(671, '^^A<<^AvvA>>vA'),(279, '^<A^^<A>>AvvvA'),(83, '<A^^^A>vvAvA'),(974, '^^^A<<AvA>>vvA'),(386, '^A^^<Av>AvvA')]:
        combs = []
        seen = set()
        parts = []

        for substr in initial.split('A'):
            parts.append([''.join(x) for x in set(permutations(substr))])

        print(initial, parts)


        starts = ['A' + 'A'.join(x) for x in product(*parts)]
        starts = ['A^^^A<<AvA>v>vA', 'A^^^A<<AvA>vv>A', 'A^^^A<<AvA>>vvA', 'A^^^A<<AvAv>v>A', 'A^^^A<<AvAv>>vA']
        print(initial, starts)

        start_q = [(start, '') for start in starts]
        # for ini in starts:
        #     print('min_length', ini, min_length(ini))
        for q, sin, sout in BFS(start_q):
            if (sin, sout) in seen:
                continue
            seen.add((sin, sout))
            if len(sin) < 2:
                combs.append(sout)
                continue
            for cand in paths[(sin[0], sin[1])]:
                q.append((sin[1:], sout + cand))
        combs2 = []
        for line in combs:
            seen = set()
            for q, sin, sout in DFS(('A' + line, '')):
                if (sin, sout) in seen:
                    continue
                seen.add((sin, sout))
                if len(sin) < 2:
                    combs2.append(sout)
                    break
                for cand in paths[(sin[0], sin[1])]:
                    q.append((sin[1:], sout + cand))
        mn = min(len(line) for line in combs2)
        print(k, mn, mn * k)
        ans += mn* k
    return ans

    for a, b in pairwise('A' + '<A^A<^^AvvvA'):
        next_pad += paths[(a, b)]
    print(next_pad)
    next_next_pad = ''
    for a, b in pairwise('A' + next_pad):
        next_next_pad += paths[(a, b)]
    print(next_next_pad, len(next_next_pad))
    return ans

if __name__ == '__main__':
    pass
