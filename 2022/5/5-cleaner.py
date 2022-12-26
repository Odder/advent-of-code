def main(direction=-1):
    with open('input', 'r') as f:
        # Read input
        stacks = ['' for _ in range(len(f.readline()) // 4)]
        f.seek(0)  # Reset file pointer
        for line in f:
            if line[1] == '1': break
            for i, cargo in enumerate(line[1::4]):
                stacks[i] = cargo + stacks[i]
        stacks = [x.strip() for x in stacks]
        f.readline()

        # Solve problem
        for line in f:
            n, a, b = (int(x) for x in line.strip().split()[1::2])
            stacks[b-1] += stacks[a-1][-n:][::direction]
            stacks[a-1] = stacks[a-1][:-n]
    return ''.join([stack[-1] for stack in stacks])


if __name__ == '__main__':
    print(f'Part 1: {main()}')
    print(f'Part 2: {main(1)}')
