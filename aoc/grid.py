def dirs(diagonal=False):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if diagonal:
        directions.extend([(1, 1), (1, -1), (-1, -1), (-1, 1)])
    return directions


class Grid:
    def __init__(self, cells):
        self.cells = cells

    def wrap(self, coord):
        x, y = coord
        x = x if 0 <= x < len(self.cells) else x + len(self.cells) % len(self.cells)
        y = y if 0 <= y < len(self.cells[x]) else y + len(self.cells[x]) % len(self.cells[x])
        return x, y

    def neighs(self, coord, diagonal=False):
        x, y = coord
        return (self.wrap((x + dx, y, dy)) for dx, dy in dirs(diagonal=diagonal))


