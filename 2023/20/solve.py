from algas.input import lines, tokens
from algas.spaces.s2 import neighbours, directions_all, indices, in_bounds, rotate
from algas.misc import Cyclic
from algas.aoc.aoc import part1, part2, part1and2
from algas.search import BFS
from functools import cache
from collections import Counter, defaultdict, deque
import re
import math


@part1(1000)
def solve1(n):
    mapping = {
        'broadcaster': ('x', ('xr', 'mr', 'rg', 'sv'), None)
    }

    for line in lines():
        a, b = line.split(' -> ')
        if a[0] == '%':
            mapping[a[1:]] = ('%', tuple(b.split(', ')), False)
        if a[0] == '&':
            mapping[a[1:]] = ('&', tuple(b.split(', ')), {})

    for key in mapping:
        t, connections, _ = mapping[key]
        for b_key in connections:
            if b_key not in mapping:
                continue
            b_t, __, ___ = mapping[b_key]
            if b_t == '&':
                mapping[b_key][2][key] = False

    k_l, k_h = 0, 0

    for _ in range(n):
        # print('----')
        for q, label, pulse, source in BFS(('broadcaster', False, None)):
            # print('pulsing', source, label, pulse)
            if pulse:
                k_l += 1
            else:
                k_h += 1
            if label not in mapping:
                continue
            t, cxs, extra = mapping[label]
            if t == '%' and not pulse:
                mapping[label] = (t, cxs, not extra)
                for cx in cxs:
                    q.append((cx, not extra, label))
            if t == '&':
                mapping[label][2][source] = pulse
                for cx in cxs:
                    if all(extra.values()):
                        q.append((cx, False, label))
                    else:
                        q.append((cx, True, label))
            if t == 'x':
                for cx in cxs:
                    q.append((cx, False, label))

    return k_h * k_l


@part2()
def solve2():
    mapping = {
        'broadcaster': ('x', ('xr', 'mr', 'rg', 'sv'), None)
    }

    for line in lines():
        a, b = line.split(' -> ')
        if a[0] == '%':
            mapping[a[1:]] = ('%', tuple(b.split(', ')), False)
        if a[0] == '&':
            mapping[a[1:]] = ('&', tuple(b.split(', ')), {})

    for key in mapping:
        t, connections, _ = mapping[key]
        for b_key in connections:
            if b_key not in mapping:
                continue
            b_t, __, ___ = mapping[b_key]
            if b_t == '&':
                mapping[b_key][2][key] = False

    k_l, k_h = 0, 0
    m = 0
    cycles = [0, 0, 0, 0]
    seen = [[], [], [], [], [], [], [], []]
    while True:
        m += 1
        for q, label, pulse, source in BFS(('broadcaster', False, None)):
            if label == 'kz':
                for i, child in enumerate(mapping[label][2]):
                    if mapping[label][2][child]:
                        seen[i].append(m)
                    if mapping[label][2][child] and not cycles[i]:
                        cycles[i] = m
                    if all(cycles):
                        return math.lcm(*cycles)
            if label == 'rx' and not pulse:
                return k_l * k_h, m
            if pulse:
                k_l += 1
            else:
                k_h += 1
            if label not in mapping:
                continue
            t, cxs, extra = mapping[label]
            if t == '%' and not pulse:
                mapping[label] = (t, cxs, not extra)
                for cx in cxs:
                    q.append((cx, not extra, label))
            if t == '&':
                mapping[label][2][source] = pulse
                for cx in cxs:
                    if all(extra.values()):
                        q.append((cx, False, label))
                    else:
                        q.append((cx, True, label))
            if t == 'x':
                for cx in cxs:
                    q.append((cx, False, label))


if __name__ == '__main__':
    pass
