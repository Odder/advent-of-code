from aoc.input import lines
from aoc.aoc import part1, part2


@part1()
def solve1():
    directions = ['E', 'S', 'W', 'N']
    dir_idx = 0
    dists = {
        'E': 0,
        'S': 0,
        'W': 0,
        'N': 0,
    }
    for line in lines():
        instr = line[0]
        inp = int(line[1:])

        match instr:
            case 'F':
                dists[directions[dir_idx]] += inp
            case 'R':
                dir_idx = (dir_idx + inp // 90) % 4
            case 'L':
                dir_idx = (4 + dir_idx - inp // 90) % 4
            case _:
                dists[instr] += inp

    return abs(dists['W'] - dists['E']) + abs(dists['N'] - dists['S'])


@part2()
def solve2():
    dir_idx = 0
    dists = [0, 0]
    wp_dists = [10, 1]
    for line in lines():
        instr = line[0]
        inp = int(line[1:])

        match instr:
            case 'F':
                dists = [dists[0] + inp * wp_dists[0], dists[1] + inp * wp_dists[1]]
            case 'R':
                for _ in range(inp // 90):
                    wp_dists[0], wp_dists[1] = wp_dists[1], -wp_dists[0]
                dir_idx = (dir_idx + inp // 90) % 4
            case 'L':
                for _ in range(inp // 90):
                    wp_dists[0], wp_dists[1] = -wp_dists[1], wp_dists[0]
            case 'N':
                wp_dists = [wp_dists[0], wp_dists[1] + inp]
            case 'S':
                wp_dists = [wp_dists[0], wp_dists[1] - inp]
            case 'E':
                wp_dists = [wp_dists[0] + inp, wp_dists[1]]
            case 'W':
                wp_dists = [wp_dists[0] - inp, wp_dists[1]]

    return abs(dists[0]) + abs(dists[1])

if __name__ == '__main__':
    pass
