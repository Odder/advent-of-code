from algas.input import lines
from algas.aoc.aoc import part1, part2, part1and2
from itertools import combinations
import z3


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None, None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

@part1(42)
def solve1(n):
    bmin = 200000000000000
    bmax = 400000000000000
    hailstones = []
    for line in lines():
        coord, vel = line.split(' @ ')
        coord = [int(x) for x in coord.split(', ')]
        vel = [int(x) for x in vel.split(', ')]
        hailstones.append((coord, vel))

    total = 0
    for (a, va), (b, vb) in combinations(hailstones, 2):
        x, y = line_intersection((a, (a[0]+va[0], a[1]+va[1], a[2]+va[2])), (b, (b[0]+vb[0], b[1]+vb[1], b[2]+vb[2])))
        if x is None:
            continue

        dx = x - a[0]
        dy = y - a[1]
        if not ((dx > 0) == (va[0] > 0) and (dy > 0) == (va[1] > 0)):
            continue

        dx = x - b[0]
        dy = y - b[1]
        if not ((dx > 0) == (vb[0] > 0) and (dy > 0) == (vb[1] > 0)):
            continue

        if bmin <= x <= bmax and bmin <= y <= bmax:
            total += 1

    return total


@part2(42)
def solve2(n):
    x, y, z, vx, vy, vz = (z3.BitVec(x, 64) for x in ['x', 'y', 'z', 'vx', 'vy', 'vz'])
    hailstones = []
    for line in lines():
        coord, vel = line.split(' @ ')
        coord = [int(x) for x in coord.split(', ')]
        vel = [int(x) for x in vel.split(', ')]
        hailstones.append((coord, vel))

    s = z3.Solver()

    # For each hailstone, set up equations based on the time of collision and position
    for i, (position, velocity) in enumerate(hailstones):
        xi, yi, zi = position
        vxi, vyi, vzi = velocity

        # Calculate time of collision based on provided example details
        ti = z3.BitVec(f't_{i}', 64)

        # Equations for position of rock and hailstone at collision time
        s.add(x + vx * ti == xi + vxi * ti)
        s.add(y + vy * ti == yi + vyi * ti)
        s.add(z + vz * ti == zi + vzi * ti)

    print(s.check())
    m = s.model()

    print(m.evaluate(x), m.evaluate(y), m.evaluate(z))


if __name__ == '__main__':
    pass
