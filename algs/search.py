from collections import deque
import heapq


class DFS:
    def __init__(self, start):
        if isinstance(start, list):
            self.stack = deque(start)
        else:
            self.stack = deque([start])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        return self, *self.stack.pop()

    def append(self, item):
        self.stack.append(item)


class BFS:
    def __init__(self, start):
        if isinstance(start, list):
            self.queue = deque(start)
        else:
            self.queue = deque([start])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.queue:
            raise StopIteration

        return self, *self.queue.popleft()

    def append(self, item):
        self.queue.append(item)


class PFS:
    def __init__(self, start):
        if isinstance(start, list):
            self.heap = start
        else:
            self.heap = [start]
        self.heap = [start]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.heap:
            raise StopIteration

        return self, *heapq.heappop(self.heap)

    def append(self, item):
        heapq.heappush(self.heap, item)


if __name__ == '__main__':
    import time

    def run_test(search_class, iterations):
        start_time = time.time()
        for q, i in search_class((0,)):
            if i < iterations:
                q.append((i+1,))
        end_time = time.time()
        return end_time - start_time

    # Number of iterations
    iterations = int(1e7)

    # Running the tests
    dfs_duration = run_test(DFS, iterations)
    bfs_duration = run_test(BFS, iterations)
    pfs_duration = run_test(PFS, iterations)

    print(f"DFS Duration: {dfs_duration} seconds")
    print(f"BFS Duration: {bfs_duration} seconds")
    print(f"PFS Duration: {pfs_duration} seconds")
