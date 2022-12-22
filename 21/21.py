from collections import deque

def read():
    with open('input', 'r') as file:
        monkeys = {}
        for line in file:
            monkey, op = line.strip().split(': ')
            monkeys[monkey] = op if ' ' in op else int(op)
    return monkeys


def get_value_of_monkey(mnky, humn=0):
    monkeys = read()
    if humn:
        monkeys['humn'] = humn

    def get_val(monkey):
        op = str(monkeys[monkey]).split()
        if len(op) > 1:
            monkeys[monkey] = eval(f'{get_val(op[0])} {op[1]} {get_val(op[2])}')
            if monkey == mnky:
                return monkeys[monkey], monkeys[op[0]], monkeys[op[2]]
        return monkeys[monkey]

    return get_val(mnky)


def part1():
    return get_value_of_monkey('root')[0]


def part2():
    _, a, b = get_value_of_monkey('root', humn=-1)
    prev_a, prev_b, prev_x = a, b, -1
    x = int(input('Start > '))
    _, a, b = get_value_of_monkey('root', humn=x)
    while a != b:
        delta = (b - a) - (prev_b - prev_a)
        delta_x = x - prev_x
        forecast = (b-a) // (delta / delta_x)
        x += int(input(f'Forecast: {-forecast} > '))
        _, a, b = get_value_of_monkey('root', humn=x)
        print(f'Diff: {b - a}')
    return x


if __name__ == '__main__':
    print(f'Part 1:', part1())
    print(f'Part 2:', part2())
