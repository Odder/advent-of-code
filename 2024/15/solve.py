from collections import deque

from algs.spaces.imaginary_s2 import load_grid, indices
from aoc.input import lines
from aoc.aoc import part1, part2


@part1()
def solve1(ans=0):
    grid = load_grid(lines())
    commands = ''.join(lines('input2'))
    you = indices(grid, '@')[0]
    dirs = {'^': -1, '>': 1j, 'v': 1, '<': -1j}
    for cmd in commands:
        d = dirs[cmd]
        k = 1
        while grid[you + k*d] == 'O':
            k += 1
        if grid[you + k*d] == '#':
            continue
        while k > 1:
            grid[you + k*d], grid[you + (k-1)*d] = grid[you + (k-1)*d], grid[you + k*d]
            k-=1
        you += d

    for box in indices(grid, 'O'):
        ans += 100*box.real + box.imag
    return ans

def gp(grid):
    for i in range(10):
        print(''.join([grid[i+(0.5*j)*1j] if grid[i+(0.5*j)*1j] else ' ' for j in range(20)]))

@part2()
def solve2(ans=0):
    grid = load_grid(lines())
    commands = ''.join(lines('input2'))
    you = indices(grid, '@')[0]
    dirs = {'^': -1, '>': 1j, 'v': 1, '<': -1j}
    for cmd in commands:
        d = dirs[cmd]
        k = 1
        if cmd in '<>':
            if cmd == '>':
                k -= 0.5
            while grid[you + k * d] == 'O':
                k += 1
            if grid[you + k * d] == '#':
                continue
            while k > 1:
                grid[you + (k - 0.5) * d], grid[you + (k - 1) * d] = grid[you + (k - 1) * d], grid[you + (k - 0.5) * d]
                k -= 1
            grid[you], grid[you + k * d] = grid[you + k * d], grid[you]
            you += 0.5 * d
        else:
            q = deque([you])
            boxes = []
            hits_wall = False
            while q:
                pos = q.popleft()
                if grid[pos+d] == '#' or grid[pos+d-0.5j] == '#' or (grid[pos-0.5j] == 'O' and grid[pos+d-1j] == '#'):
                    hits_wall = True
                    break
                if grid[pos+d] == 'O':
                    q.append(pos+d)
                    q.append(pos+d + 0.5j)
                    boxes.append(pos+d)
                if grid[pos+d - 0.5j] == 'O':
                    q.append(pos+d)
                    q.append(pos+d - 0.5j)
                    boxes.append(pos+d - 0.5j)

            if hits_wall:
                continue

            seen = set()
            for box in boxes[::-1]:
                if box in seen:
                    continue
                grid[box], grid[box+d] = grid[box+d], grid[box]
                seen.add(box)
            grid[you], grid[you + d] = grid[you +d], grid[you]
            you = you + d

    # gp(grid)
    for box in indices(grid, 'O'):
        ans += 100 * box.real + 2*box.imag

    return ans

if __name__ == '__main__':
    pass
