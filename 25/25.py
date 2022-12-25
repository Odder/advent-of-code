def to_snafu(num):
    digits = '=-012'
    total = ''
    while num:
        total = digits[(num + 2) % 5] + total
        num = (num + 2) // 5
    return str(total)


def from_snafu(snafu):
    k = 0
    snafu = list(snafu)
    total = 0
    digits = {
        '=': -2,
        '-': -1,
        '0': 0,
        '1': 1,
        '2': 2,
    }
    while snafu:
        digit = snafu.pop()
        total += digits[digit] * 5**k
        k += 1
    return total


def read():
    with open('input', 'r') as file:
        nums = list(map(from_snafu, [str(x.strip()) for x in file]))
    return nums


def part1():
    ans = sum(read())
    return to_snafu(ans)


if __name__ == '__main__':
    print(f'Part 1:', part1())
