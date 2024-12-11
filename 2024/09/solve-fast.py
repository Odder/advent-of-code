from heapq import heappush, heappop
from aoc.input import lines
from aoc.aoc import part2

@part2()
def solve3():
    line = [int(x) for x in list(lines())[0]]
    reverse_disk = []
    gaps = [[] for _ in range(10)]
    pos = 0
    total = 0
    int_sum = lambda a, b: (b*(b+1) - a*(a+1)) // 2

    for i, reps in enumerate(line):
        if i % 2 == 1:
            heappush(gaps[reps], pos)
        else:
            reverse_disk.append((pos, i//2, int(reps)))
        pos += reps

    while reverse_disk:
        pos, char, reps = reverse_disk.pop()
        target_pos, k = min((gaps[k][0], k) for k in range(reps, 10))
        if target_pos < pos:
            heappop(gaps[k])
            if k != reps:
                heappush(gaps[k-reps], (target_pos+reps))
            total += char * int_sum(target_pos-1, target_pos+reps-1)
        else:
            total += char * int_sum(pos-1, pos+reps-1)

    return total

if __name__ == '__main__':
    pass
