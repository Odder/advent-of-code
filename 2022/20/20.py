from collections import deque


def decrypt(rounds=1, multiplier=1):
    with open('input', 'r') as file:
        msg = deque([(int(x) * multiplier, i) for i, x in enumerate(file)])

    order = list(msg)
    for _ in range(rounds):
        for n in order:
            msg.rotate(-msg.index(n))       # [n_comes_from_here, ...]
            msg.popleft()                   # Remove n
            msg.insert(n[0] % len(msg), n)  # Insert n at the nth offset
    msg = deque([n for n, _ in msg])
    msg.rotate(-msg.index(0))  # [0, ...]
    return sum([msg[k] for k in (1000, 2000, 3000)])


if __name__ == '__main__':
    print(f'Part 1:', decrypt())
    print(f'Part 2:', decrypt(10, 811589153))
