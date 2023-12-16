from algas.input import tokens
from algas.spaces.vectors import V
from algas.aoc.aoc import part1, part2


directions = {
    'U': V((-1, 0)),
    'D': V((1, 0)),
    'R': V((0, 1)),
    'L': V((0, -1))
}


@part2(9)
@part1(1)
def main(n):
    rope = [V((0, 0)) for _ in range(n+1)]
    visited = set()
    for move, dist in tokens():
        v = directions[move]
        for _ in range(int(dist)):
            rope[0] += v
            for i in range(1, len(rope)):
                diff_v = rope[i] - rope[i-1]
                if not (V((-2, -2)) < diff_v < V((2, 2))):
                    rope[i] -= diff_v.normalise()
            visited |= {str(rope[-1].data)}
    return len(visited)


if __name__ == '__main__':
    pass
