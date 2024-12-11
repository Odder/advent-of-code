from aoc.input import lines
from aoc.aoc import part1, part2


@part1()
def solve1():
    disk = []
    line = list(lines())[0]
    for i, char in enumerate(line):
        if i % 2 ==  0:
            for _ in range(int(char)):
                disk.append((i//2))
        else:
            for _ in range(int(char)):
                disk.append('.')

    while True:
        first_dot = disk.index('.')
        last_number = 0
        for i in range(len(disk)):
            if disk[len(disk)-1-i] != '.':
                last_number = len(disk)-1-i
                break
        if first_dot - last_number == 1:
            break
        disk[first_dot], disk[last_number] = disk[last_number], disk[first_dot]
    return sum(i*int(x) for i, x in enumerate(disk) if x != '.')

@part2()
def solve2():
    line = [int(x) for x in list(lines())[0]]
    disk = []
    disk_r = []

    for i, char in enumerate(line):
        if i % 2 ==  0:
            disk.append((i//2, int(char)))
            for _ in range(int(char)):
                disk_r.append((i//2))
        else:
            disk.append(('.', int(char)))
            for _ in range(int(char)):
                disk_r.append('.')

    for i in range(len(disk)):
        if disk[len(disk)-1-i][0] != '.':
            for j in range(len(disk)-1-i):
                if disk[j][0] == '.' and disk[j][1] >= disk[len(disk)-i-1][1]:
                    a = disk[j]
                    b = disk[len(disk)-i-1]
                    if a[1] == b[1]:
                        disk[j], disk[len(disk)-i-1] = b, a
                    else:
                        disk[j] = b
                        disk[len(disk)-i-1] = a[0], b[1]
                        disk = disk[:j+1] + [('.', a[1]-b[1])] + disk[j+1:]
                        i += 1
                    break

    flat_disk = []
    for i, x in disk:
        flat_disk += [i] * x
    return sum(i*int(x) for i, x in enumerate(flat_disk) if x != '.')

if __name__ == '__main__':
    pass
