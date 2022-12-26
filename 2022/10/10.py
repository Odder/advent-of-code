def part1():
    with open('input', 'r') as file:
        t, total, duration, reward = 1, 1, 1, 0
        timeline = []
        commands = [line.strip().split() for line in file][::-1]
        while len(commands) and duration > 0:
            duration -= 1
            if duration == 0:
                total += reward
                command = commands.pop()
                if command[0] == 'noop':
                    duration, reward = 1, 0
                else:
                    duration, reward = 2, int(command[1])
            timeline.append((t, total))
            t += 1
    return timeline


def part2(timeline):
    screen = ''
    for t, x in timeline:
        screen += '#' if abs(x - ((t-1) % 40)) < 2 else '.'
        if len(screen) == 40:
            print(screen)
            screen = ''


if __name__ == '__main__':
    tl = part1()
    print(f'Part 1: {sum([t*x for t, x in tl if ((t + 20) % 40) == 0])}')
    print(f'Part 2:')
    part2(tl)
