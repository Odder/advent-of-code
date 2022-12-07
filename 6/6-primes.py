PRIME_MAP = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37,
             'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83,
             'x': 89, 'y': 97, 'z': 101}


def main(n):
    with open('input', 'r') as f:
        line = f.readline()
        total = 1
        i, j = 0, 0
        while j - i < n:
            if total % PRIME_MAP[line[j]] == 0:
                while True:
                    total //= PRIME_MAP[line[i]]
                    i += 1
                    if line[i-1] == line[j]:
                        break
            total *= PRIME_MAP[line[j]]
            j += 1

        return j


if __name__ == '__main__':
    print(f'Part 1: {main(4)}')
    print(f'Part 2: {main(14)}')
