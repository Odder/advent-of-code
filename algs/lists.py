"""
This module gives you a collection of tools to handle iterables.
"""
import heapq
from itertools import islice
from math import ceil
from typing import Iterator, Union


lmap = lambda f, it: list(map(f, it))
cnt = lambda it: sum(1 for x in it if x)

def group(it: list[object], splitter: object = None) -> Iterator[list[object]]:
    """
    Groups items within an iterator into lists using a separator element.
    By default the separator item is None.

    example:
    ```python
    a = [1,2,3,None,4,5,None,6]
    group(a)
    # [[1,2,3], [4,5], [6]]


    a = [1,2,1,4,5,1,6]
    group(a, splitter=1)
    # [[2], [4,5], [6]]
    ```
    """
    grp: list[object] = []
    for x in it:
        if x == splitter:
            yield grp
            grp = []

        else:
            grp.append(x)
    yield grp

def flatten(it):
    out = []
    for x in it:
        out.extend(x)
    return out

def nwise(it, n=2, rev=False):
    if not rev:
        return zip(*[islice(it, i, None) for i in range(n)])
    return zip(*[islice(list(it)[::-1], i, None) for i in range(n)][::-1])

def divide(it, slices=2):
    """
    Evenly groups items within an iterator into n evenly sized groups.

    example:
    ```python
    a = [1,2,3,4,5,6,7,8,9]
    divide(a, 3)
    # [[1,2,3], [4,5,6], [7,8,9]]
    ```
    """
    lst = list(it)
    length = len(lst)
    k = 0
    while k < length:
        size = ceil((length - k) / slices)
        yield lst[k:min(k+size, length)]
        k += size
        slices -= 1


def grouping(it, n=2):
    """
    Evenly groups items within an iterator into groups of size n.

    example:
    ```python
    a = [1,2,3,4,5,6,7,8,9]
    divide(a, 2)
    # [[1,2], [2,3], [4,5], [6,7], [8,9]]
    ```
    """
    current = []
    i = 0
    for x in it:
        i += 1
        current.append(x)
        if i % n == 0:
            yield current
            current = []


def top_n(it, n=1, val=lambda x: x):
    """
    Given a list of numbers we want to find the biggest n elements.
    The elements will be returned in a random order

    example:
    ```python
    a = [1,2,3,4,5,6,7,8,9]
    top_n(a, 2)
    # [8, 9]

    a = [2, 3, 4, 5, 6, 7, 8, 12]
    top_n(a, 2, number_of_divisors)
    # [12, 6]
    ```
    """
    top = []

    for x in it:
        heapq.heappush(top, val(x))
        if len(top) > n:
            heapq.heappop(top)

    return (x for x in top)


if __name__ == '__main__':
    assert list(group([1, 2, 3, 4])) == [[1, 2, 3, 4]]
    assert list(group(['1', 1, [1]])) == [['1', 1, [1]]]
    assert list(group([1, 2, 3, None, 4, 5, None, 6])) == [[1, 2, 3], [4, 5], [6]]
    assert list(group(['1', 1, [1]], splitter=1)) == [['1'], [[1]]]
    assert list(group([1, 2, 1, 2, 1], splitter=1)) == [[], [2], [2], []]
    assert list(group([])) == [[]]

    assert list(divide([])) == []
    assert [len(x) for x in divide([1, 2, 3, 4], 2)] == [2, 2]
    assert [len(x) for x in divide([1, 2, 3], 2)] == [2, 1]
    assert [len(x) for x in divide([1, 2, 3, 4, 5, 6, 7, 8], 3)] == [3, 3, 2]
    print([len(x) for x in divide([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 4)])
    assert [len(x) for x in divide([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 4)] == [4, 4, 4, 3]

    print(list(divide([1,2,3,4,5,6,7,8,9], 2)))
    print(list(divide([1,2,3,4,5,6,7,8,9], 3)))
    print(list(divide([1,2,3,4,5,6,7,8,9], 4)))

    print(list(grouping([1,2,3,4,5,6,7,8,9], 2)))
    print(list(grouping([1,2,3,4,5,6,7,8,9], 3)))
    print(list(grouping([1,2,3,4,5,6,7,8,9], 4)))

    print(list(top_n([1,2,3,4,5,6,7,8,9], 1)))
    print(list(top_n([1,2,3,4,5,6,7,8,9], 3)))
    print(list(top_n([9,8,7,6,5,4,3,2,1], 1)))
    print(list(top_n([9,8,7,6,5,4,3,2,1], 3)))

    print('-----')
    for x in nwise([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, rev=True):
        print(x)


