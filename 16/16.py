from re import findall
from collections import deque, defaultdict
import os


def clear():
    print('\n'*100)


def read():
    nodes = {}
    with open('input', 'r') as file:
        for line in file:
            m = findall('([A-Z]{2}|[0-9]+)', line)
            label, flow, *neighs = m
            nodes[label] = int(flow), neighs

    return nodes


def part1():
    nodes = read()
    simplified = {}
    for n in nodes:
        if nodes[n][0] == 0 and n != 'AA':
            continue
        q = deque([(n, 0, 'NONE')])
        while q:
            curr, depth, prev = q.popleft()
            if depth > 20:
                continue
            flow, neighs = nodes[curr]
            visited = {}
            if curr in visited:
                continue
            else:
                visited[curr] = True
            if flow > 0 and curr != n:
                if curr <= n:
                    continue

                label = f'{nodes[n][0]} {nodes[curr][0]}'
                if label in simplified:
                    simplified[label] = min(simplified[label], depth)
                else:
                    simplified[label] = depth
                continue

            for neigh in neighs:
                if neigh == prev or neigh in visited:
                    continue
                q.append((neigh, depth + 1, curr))
    graph = defaultdict(list)
    for l in simplified:
        a, b = l.split()
        graph[a].append((b, simplified[l]))
        graph[b].append((a, simplified[l]))

    return graph


def play():
    graph = part1()
    pos = '0'
    pos_e = '0'
    flow = 0
    score = 0
    walking = 0
    walking_e = 0
    t = 0
    opened = {}
    path = ['0']
    path_e = ['0']
    while t < 26:
        t += 1
        score += flow
        if walking > 0 and walking_e > 0:
            walking -= 1
            walking_e -= 1
            continue
        print(f'==========================================================')
        print(f' t: {t}  flow: {flow}  score: {score}')
        print(f'----------------------------------------------------------')
        print(f'')
        print(f' You are currently @ {pos}')
        print(f'')
        while walking == 0:
            if pos not in opened:
                if input('Do you want to open valve? '):
                    opened[pos] = True
                    flow += int(pos)
                    print(f'')
                    print(f'The valve has been opened')
                    print(f'')
                    break
                print(f'')
            print(f'You have following options of where you want to continue:')
            options = {}
            for neigh, cost in graph[pos]:
                cost_label = f' dist: {cost}'
                visited_label = ' (already opened)' if neigh in opened else ''
                options[neigh] = int(cost)
                print(f' > {neigh}{cost_label}{visited_label}')
            to = 'qqq'
            while to not in options:
                print(f'')
                to = input(f' > ')
                print(f'')
            pos = to
            path.append(pos)
            walking = options[pos] - 1
            break
        else:
            walking -= 1

        while walking_e == 0:
            print(f'----------------------------------------------------------')
            print(f'')
            print(f' Elephant currently @ {pos_e}')
            print(f'')
            if pos_e not in opened:
                if input('Should the Elephant open the valve? '):
                    opened[pos_e] = True
                    flow += int(pos_e)
                    print(f'')
                    print(f'The valve has been opened')
                    print(f'')
                    break
                print(f'')
            print(f'The elephant has following options of where he can go:')
            options = {}
            for neigh, cost in graph[pos_e]:
                cost_label = f' dist: {cost}'
                visited_label = ' (already opened)' if neigh in opened else ''
                options[neigh] = int(cost)
                print(f' > {neigh}{cost_label}{visited_label}')
            to = 'qqq'
            while to not in options:
                print(f'')
                to = input(f' > ')
            pos_e = to
            path_e.append(pos_e)
            walking_e = options[pos_e] - 1
            break
        else:
            walking_e -= 1

    print(f'==========================================================')
    print(f' t: 26  flow: {flow}  score: {score}')
    print(f'----------------------------------------------------------')
    print(' -> '.join(path))
    print(' -> '.join(path_e))


def part2():
    return


if __name__ == '__main__':
    play()
