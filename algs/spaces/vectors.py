class V:
    def __init__(self, vector):
        self.data = list(vector)
        self.n = 0

    def normalise(self):
        self.data = [x//abs(x) if x else 0 for x in self.data]
        return self

    def __add__(self, other):
        return V(tuple((a + b) for a, b in zip(self.data, other.data)))

    def __sub__(self, other):
        return V(tuple((a - b) for a, b in zip(self.data, other.data)))

    def __repr__(self):
        vals = ', '.join(str(x) for x in self.data)
        return f'Vector({vals})'

    def __le__(self, other):
        return all(a <= b for a, b in zip(self.data, other.data))

    def __ge__(self, other):
        return all(a >= b for a, b in zip(self.data, other.data))

    def __gt__(self, other):
        return all(a > b for a, b in zip(self.data, other.data))

    def __eq__(self, other):
        return all(a == b for a, b in zip(self.data, other.data))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return V(tuple(x * other for x in self.data))
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        if self.n > len(self.data):
            raise StopIteration
        return self.data[self.n-1]


if __name__ == '__main__':
    print(V((2, 3)))
    print(tuple(V((2, 3))))
    print(V(V((2, 3))))