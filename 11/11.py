class Monkey:
    def __init__(self, items, worry, test, targets):
        self.items = items
        self.worry = worry
        self.test = test
        self.targets = targets
        self.inspections = 0

    def inspect(self, stress_factor=3):
        item = self.items.pop()
        item = self.worry(item) // stress_factor
        target = self.targets[int(item % self.test > 0)]
        self.inspections += 1
        return item, target

    def give(self, item):
        self.items.append(item)

    def __repr__(self):
        items = ', '.join(str(x) for x in self.items)
        return f'Monkey did {self.inspections: >3} inspection and current has following items: {items}'


def read():
    monkeys = [
        Monkey([59, 65, 86, 56, 74, 57, 56], lambda x: x*17, 3, (3, 6)),
        Monkey([63, 83, 50, 63, 56], lambda x: x+2, 13, (3, 0)),
        Monkey([93, 79, 74, 55], lambda x: x+1, 2, (0, 1)),
        Monkey([86, 61, 67, 88, 94, 69, 56, 91], lambda x: x+7, 11, (6, 7)),
        Monkey([76, 50, 51], lambda x: x*x, 19, (2, 5)),
        Monkey([77, 76], lambda x: x+8, 17, (2, 1)),
        Monkey([74], lambda x: x*2, 5, (4, 7)),
        Monkey([86, 85, 52, 86, 91, 95], lambda x: x+6, 7, (4, 5)),
    ]

    return monkeys


def inspection_time(n=20, stress_factor=3, mod=9699690):
    monkeys = read()
    for _ in range(n):
        for monkey in monkeys:
            while monkey.items:
                item, target = monkey.inspect(stress_factor)
                monkeys[target].give(item % mod)
    return monkeys


def part1():
    for monkey in inspection_time():
        print(monkey)
    print()


def part2():
    for monkey in inspection_time(10_000, stress_factor=1):
        print(monkey)
    print()


if __name__ == '__main__':
    print(f'Part 1:')
    part1()
    print(f'Part 2:')
    part2()
