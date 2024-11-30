from functools import reduce
from operator import mul

def prod(numbers):
    return reduce(mul, numbers)


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y


def crt_pair(a1, n1, a2, n2):
    gcd, s, t = extended_gcd(n1, n2)
    if (a2 - a1) % gcd != 0:
        return None, None
    lcm = n1 * n2 // gcd
    mul = (a2 - a1) // gcd
    x = (a1 + n1 * s * mul) % lcm
    return x, lcm


def crt(congruences):
    return reduce(lambda acc, curr: crt_pair(*acc, *curr), congruences)


def shunting_yard(expr, precedence = None, apply_op = None):
    precedence = precedence if precedence else {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    apply_op = apply_op if apply_op else lambda op, a, b: eval(f'{b} {op} {a}')

    output = []
    operators = []

    for token in expr.split():
        match token:
            case t if t.isdigit():
                output.append(int(t))
            case t if t in precedence:
                while (operators and
                       operators[-1] != '(' and
                       (precedence[operators[-1]] > precedence[t] or
                           (precedence[operators[-1]] == precedence[t]))):
                    output.append(operators.pop())
                operators.append(t)
            case '(':
                operators.append(token)
            case ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                if operators and operators[-1] == '(':
                    operators.pop()

    output.extend(operators[::-1])

    eval_stack = []
    for token in output:
        if isinstance(token, int):
            eval_stack.append(token)
        else:
            b = eval_stack.pop()
            a = eval_stack.pop()
            eval_stack.append(apply_op(token, a, b))

    return eval_stack[0]