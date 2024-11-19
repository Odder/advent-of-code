class Cyclic:
    def __init__(self, n):
        self.n = n
        self.idx = -1
        self.seen = {}
        self.curr = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx > self.n:
            raise StopIteration

        if self.curr in self.seen:
            cycle_length = self.idx - self.seen[self.curr]
            if (self.idx+1) % cycle_length == self.n % cycle_length:
                raise StopIteration

        self.seen[self.curr] = self.idx
        self.idx += 1
        return self.see, self.idx

    def see(self, curr):
        self.curr = curr


if __name__ == '__main__':
    cyclic = [1,2,3,4,5,6,7,8,9,6,7,8,9,6,7,8,9,6,7,8,9]
    for see, i in Cyclic(13):
        see(cyclic[i])

    print(cyclic[i])