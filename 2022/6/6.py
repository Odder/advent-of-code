def main(n):
    with open('input', 'r') as f:
        line = f.readline()
        for i in range(n, len(line)):
            if len(set(line[i-n:i])) == n:
                return i


if __name__ == '__main__':
    print(f'Part 1: {main(4)}')
    print(f'Part 2: {main(14)}')
