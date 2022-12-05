def main(stack_order=True):
    with open('input', 'r') as f:
        for i in range(10):
            f.readline()
        stacks = [
            list('DBJV'),
            list('PVBWRDF'),
            list('RGFLDCWQ'),
            list('WJPMLNDB'),
            list('HNBPCSQ'),
            list('RDBSNG'),
            list('ZBPMQFSH'),
            list('WLF'),
            list('SVFMR'),
        ]

        for line in f:
            n, a, b = (int(x) for x in line.strip().split()[1::2])
            for _ in range(n):
                x = stacks[a-1].pop()
                stacks[b-1].append(x)
            if not stack_order:
                stacks[b-1][-n:] = stacks[b-1][-n:][::-1]
    solution = ''.join([stack.pop() for stack in stacks])
    return solution


if __name__ == '__main__':
    print(f'Part 1: {main()}')
    print(f'Part 2: {main(False)}')
