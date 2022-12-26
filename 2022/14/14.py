from collections import defaultdict


def read():
    matrix = defaultdict(bool)
    width, height = (10e7, 0), (0, 0)
    with open('input', 'r') as file:
        for line in file:
            points = [[int(x) for x in coord.split(',')] for coord in line.strip().split(' -> ')]
            for [x1, y1], [x2, y2] in zip(points[:-1], points[1:]):
                width = (min(width[0], x1, x2), max(width[1], x1, x2))
                height = (min(height[0], y1, y2), max(height[1], y1, y2))
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    matrix[(i, y1)] = True
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    matrix[(x1, i)] = True
    return matrix, width, height


def fill_sand(has_floor=False):
    m, w, h = read()
    s = (500, 0)
    f = h[1] + 1
    for k in range(int(10e7)):
        x, y = s
        for y in range(y, int(10e7)):
            if not has_floor and not (w[0] <= x <= w[1] and h[0] <= y <= h[1]):
                return k

            if y < f and not m[(x, y + 1)]:
                continue
            elif y < f and not m[(x - 1, y + 1)]:
                x -= 1
            elif y < f and not m[(x + 1, y + 1)]:
                x += 1
            else:
                if s == (x, y):
                    return k + 1
                break
        m[(x, y)] = True


if __name__ == '__main__':
    print(f'Part 1:', fill_sand())
    print(f'Part 2:', fill_sand(True))
