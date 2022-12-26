from collections import deque

def read():
    with open('input', 'r') as file:
        return {tuple(int(x) for x in line.strip().split(',')): True for line in file}


def part1():
    droplets = read()
    surface = 6 * len(droplets)
    for x, y, z in droplets:
        for dx, dy, dz in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            if (x+dx, y+dy, z+dz) in droplets:
                surface -= 2
    return surface


def part2():
    visited = {}
    droplets = read()
    drop_q = deque([droplet for droplet in droplets])
    disjoint_surface_areas = []
    while drop_q:
        droplet_x, droplet_y, droplet_z = drop_q.popleft()
        surf_q = deque()
        for dx, dy, dz in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]:
            offset = (droplet_x + dx, droplet_y + dy, droplet_z + dz)
            if offset not in droplets and offset not in visited:
                surf_q.append((offset, 0))

        surface_area = 0
        while surf_q:
            (x, y, z), depth = surf_q.popleft()
            if (x, y, z) in visited:
                continue

            local_surface_area = 0
            to_queue = []
            for dx, dy, dz in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]:
                offset = (x + dx, y + dy, z + dz)
                if offset in droplets:
                    local_surface_area += 1
                elif offset not in visited:
                    to_queue.append(offset)

            surface_area += local_surface_area
            visited[(x, y, z)] = True

            if depth == 1 and local_surface_area == 0:
                continue

            for neigh in to_queue:
                surf_q.append((neigh, int(not bool(local_surface_area))))
        if surface_area > 0:
            disjoint_surface_areas.append(surface_area)
    return max(disjoint_surface_areas)


if __name__ == '__main__':
    print(f'Part 1:', part1())
    print(f'Part 2:', part2())
