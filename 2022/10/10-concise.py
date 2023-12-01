





def main():
    with open('input', 'r') as file:
        t, total, duration, reward = 0, 1, 1, 0
        timeline = []
        commands = [line.strip().split() for line in file][::-1]
        while len(commands) and duration > 0:
            t += 1
            duration -= 1
            if duration == 0:
                total += reward
                command = commands.pop()
                duration, reward = (1, 0) if command[0] == 'noop' else (2, int(command[1]))
            timeline.append((t, total))
            print('#' if abs(total - ((t-1) % 40)) < 2 else '.', end='' if t % 40 else '\n')

    return sum([t*x for t, x in timeline if ((t + 20) % 40) == 0])


if __name__ == '__main__':
    print(f'Part 2 (above)\nPart 1: {main()}')
