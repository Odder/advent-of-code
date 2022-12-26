from collections import deque
from functools import reduce
from re import findall


def blueprint(costs, turns):
    q, best = deque([([0, 0, 0, 0], [1, 0, 0, 0], 0)]), -1
    for k in range(2_000):
        stash, prod, depth = q.popleft()
        for round in range(depth, turns):
            options = [i for i in range(len(costs)) if min(a - b for a, b in zip(stash, costs[i])) >= 0]
            if len(options[1:]) and 4 not in options:
                for i in range(len(options)-2, -1, -1):
                    new_prod = list(prod)
                    new_prod[options[i]-1] += 1 if options[i] > 0 else 0
                    q.append(([a-b+c for a, b, c in zip(stash, costs[options[i]], prod)], new_prod, round + 1))
            stash = [a - b + c for a, b, c in zip(stash, costs[options[-1]], prod)]
            prod[options[-1] - 1] += 1 if len(options) > 1 else 0
        best = max(best, stash[-1])
    return best


if __name__ == '__main__':
    with open('input', 'r') as file:
        blueprints = []
        for line in file:
            p = [int(x) for x in findall('[0-9]+', line)]
            blueprints.append([[0, 0, 0, 0], [p[1], 0, 0, 0], [p[2], 0, 0, 0], [p[3], p[4], 0, 0], [p[5], 0, p[6], 0]])

    print('Part 1:', sum((i + 1)*blueprint(bp, 24) for i, bp in enumerate(blueprints)))
    print('Part 2:', reduce(lambda a, b: a*b, (blueprint(bp, 32) for bp in blueprints[:3]), 1))
