class Range:
    def __init__(self, left=0, right=0):
        self.left = left
        self.right = right
        self.n = 0

    def __add__(self, other):
        if isinstance(other, int):
            return Range(self.left + other, self.right + other)

    def __contains__(self, other):
        if isinstance(other, int):
            return self.left <= other <= self.right
        return self.left <= other.left and self.right >= other.right

    def __and__(self, other):
        left = max(self.left, other.left)
        right = min(self.right, other.right)
        if right < left:
            return None
        return Range(left, right)

    def __xor__(self, other):
        shades = []
        if self.left < other.left:
            shades.append(Range(self.left, other.left))
        if other.right < self.right:
            shades.append(Range(other.right, self.right))
        return shades

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __ge__(self, other):
        return self.left >= other.left

    def __lt__(self, other):
        return self.left < other.left

    def __le__(self, other):
        return self.left <= other.left

    def __ne__(self, other):
        return self.left != other.left or self.right != other.right

    def __str__(self):
        return f'Range({self.left}, {self.right})'

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        if self.n == 1:
            return self.left
        if self.n == 2:
            return self.right
        raise StopIteration


def simplify(it, is_sorted=True):
    if not is_sorted:
        it = sorted(list(it))

    left, right = next((x for x in it), (None, None))
    for l, r in it:
        if l > right:
            yield Range(left, right)
            left = l
        right = max(r, right)
    yield Range(left, right)


if __name__ == '__main__':
    a = Range(0,10)
    b = Range(5, 8)
    c = Range(11, 13)
    d = Range(9, 12)

    collection = [a, b, c, d]

    for r in collection:
        print(r)

    print('----')

    for r in sorted(collection):
        print(r)

    print('----')

    print(a)
    print(b)
    print(a & d)
    print(b in a, a in b)

    print('----')

    for r in simplify(collection):
        print(r)

