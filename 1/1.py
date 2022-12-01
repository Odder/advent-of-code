import heapq


def main(n=3):
    top_x = []
    cals = 0

    with open('input', 'r') as f:
        for line in f.read().splitlines():
            if line == "":
                if len(top_x) >= n:
                    heapq.heappushpop(top_x, cals)
                else:
                    heapq.heappush(top_x, cals)

                cals = 0
                continue
            cals += int(line)

    return sum(top_x)


if __name__ == '__main__':
    print(f'top 1: {main(1)}')
    print(f'top 3: {main(3)}')
