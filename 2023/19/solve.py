from algas.input import lines, tokens
from algas.search import BFS
from algas.aoc.aoc import part1and2


@part1and2()
def solve1():
    instructions = {}
    tests = []
    for line in lines():
        if line == '':
            continue
        if line[0] == '{':
            tests.append(line)
        else:
            label, rules = line.split('{')
            rls = []
            for rule in rules[:-1].split(','):
                parts = rule.split(':')
                if len(parts) == 1:
                    rls.append((parts[0],))
                else:
                    rls.append((parts[0], parts[1]))
            instructions[label] = rls

    total = 0
    for test in tests:
        label = 'in'
        x, m, a, s = [int(x.split('=')[1]) for x in test[1:-1].split(',')]
        while label != 'A' and label != 'R':
            for instruction in instructions[label]:
                if len(instruction) == 1:
                    label = instruction[0]
                    break
                rule, goto = instruction
                if eval(rule):
                    label = goto
                    break
        total += sum((x, m, a, s)) if label == 'A' else 0

    accepted = []
    for q, x, m, a, s, label in BFS(((1, 4000), (1, 4000), (1, 4000), (1, 4000), 'in')):
        while label != 'A' and label != 'R':
            for instruction in instructions[label]:
                if len(instruction) == 1:
                    label = instruction[0]
                    break
                rule, goto = instruction
                if '<' in rule:
                    variable, limit = rule.split('<')
                    if variable == 'x' and int(limit) > x[0]:
                        q.append(((x[0], int(limit)-1),m,a,s,goto))
                        x = (int(limit), x[1])
                    elif variable == 'm' and int(limit) > m[0]:
                        q.append((x,(m[0], int(limit)-1),a,s,goto))
                        m = (int(limit), m[1])
                    elif variable == 'a' and int(limit) > a[0]:
                        q.append((x,m,(a[0], int(limit)-1),s,goto))
                        a = (int(limit), a[1])
                    elif variable == 's' and int(limit) > s[0]:
                        q.append((x,m,a,(s[0], int(limit)-1),goto))
                        s = (int(limit), s[1])
                elif '>' in rule:
                    variable, limit = rule.split('>')
                    if variable == 'x' and int(limit) < x[1]:
                        q.append(((int(limit)+1, x[1]),m,a,s,goto))
                        x = (x[0], int(limit))
                    elif variable == 'm' and int(limit) < m[1]:
                        q.append((x,(int(limit)+1, m[1]),a,s,goto))
                        m = (m[0], int(limit))
                    elif variable == 'a' and int(limit) < a[1]:
                        q.append((x,m,(int(limit)+1, a[1]),s,goto))
                        a = (a[0], int(limit))
                    elif variable == 's' and int(limit) < s[1]:
                        q.append((x,m,a,(int(limit)+1, s[1]),goto))
                        s = (s[0], int(limit))
        if label == 'A':
            accepted.append((x, m, a, s))

    return total, sum((x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1) for x, m, a, s in accepted)


if __name__ == '__main__':
    pass
