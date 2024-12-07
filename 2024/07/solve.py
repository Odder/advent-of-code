from aoc.input import nums, lines
from aoc.aoc import part1, part2

@part2(True)
@part1(False)
def solve1(has_concat):
    total = 0
    for [target, *terms] in lines(mod=nums):
        q = [(terms[0], 1)]
        while q:
            x, depth = q.pop()
            if depth < len(terms):
                q.append((x + terms[depth], depth + 1))
                q.append((x * terms[depth], depth + 1))
                if has_concat:
                    q.append((int(str(x) + str(terms[depth])), depth + 1))
            elif x == target:
                total += target
                break
    return total

if __name__ == '__main__':
    pass
