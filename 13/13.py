from functools import cmp_to_key


def read():
    signals = []
    with open('input', 'r') as file:
        for line in file:
            signals.append((eval(line), eval(file.readline())))
            file.readline()
    return signals


def comp_order(left, right):
    if type(left) is list and type(right) is int:
        right = [right]
    if type(left) is int and type(right) is list:
        left = [left]

    if right is None:
        return 1

    for i in range(len(left)):
        if i >= len(right):
            return 1
        if type(left[i]) is list or type(right[i]) is list:
            right_order = comp_order(left[i], right[i])
            if not right_order:
                continue
            return right_order
        if not left[i] == right[i]:
            return -1 if left[i] < right[i] else 1

    if len(right) > len(left):
        return -1
    return 0


def part1():
    k = 0
    for i, (left, right) in enumerate(read()):
        order = comp_order(left, right)
        if order == -1:
            k += i + 1
    return k


def part2():
    signals = [s for sl in read() for s in sl]

    signals.append([2])
    signals.append([6])

    l, u = 0, 0
    for k, signal in enumerate(sorted(signals, key=cmp_to_key(comp_order))):
        if signal == [2]:
            l = k + 1
        if signal == [6]:
            u = k + 1

    return l * u


if __name__ == '__main__':
    print(f'Part 1:', part1())
    print(f'Part 2:', part2())
