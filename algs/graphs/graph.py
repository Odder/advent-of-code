import heapq
from typing import Hashable


class Graph:
    """
    A simple Graph implementation that only keeps track of edges.
    Nodes are implicated by inclusion in edges. And thus should be stored externally
    """

    def __init__(self):
        self.edges: dict[Hashable, list[tuple[Hashable, int]]] = {}
        self.weights: dict[tuple[Hashable, Hashable], int] = {}

    def neighbours(self, idx: Hashable) -> list[Hashable, tuple[Hashable, int]]:
        return self.edges[idx]

    def add_edge(self, idx: Hashable, target: Hashable, bidirectional: bool = False, weight: int = 1) -> None:
        if idx not in self.edges:
            self.edges[idx] = []
        self.edges[idx].append((target, weight))
        self.weights[(idx, target)] = weight

        if bidirectional:
            self.add_edge(target, idx, False, weight)
            self.weights[(target, idx)] = weight

    def remove_edge(self, idx: Hashable, target: Hashable) -> None:
        self.edges[idx].remove((target, self.weights[(idx, target)]))
        # self.edges[target].remove((idx, self.weights[(target, idx)]))


class PriorityQueue:
    """
    Simple PriorityQueue class using the heapq library
    """

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def append(self, node, priority):
        heapq.heappush(self.elements, (priority, node))

    def pop(self):
        return heapq.heappop(self.elements)[1]


import unittest


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_neighbours(self):
        self.assertEqual(len(self.graph.edges), 0)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(1, 4)
        self.graph.add_edge(4, 1)
        self.assertEqual(len(self.graph.neighbours(1)), 3)
        self.assertEqual(len(self.graph.neighbours(4)), 1)
        self.assertEqual(self.graph.neighbours(1), [(2, 1), (3, 1), (4, 1)])

        with self.assertRaises(KeyError):
            self.graph.neighbours(2)

    def test_add_edge(self):
        self.assertEqual(len(self.graph.edges), 0)
        self.graph.add_edge(1, 2)
        self.assertEqual(self.graph.edges[1], [(2, 1)])
        self.graph.add_edge('2', '3')
        self.assertEqual(self.graph.edges['2'], [('3', 1)])
        self.graph.add_edge(1, '3')
        self.assertEqual(self.graph.edges[1], [(2, 1), ('3', 1)])

        self.graph.add_edge('bi_from', 'bi_to', bidirectional=True)
        self.assertEqual(self.graph.edges['bi_from'], [('bi_to', 1)])
        self.assertEqual(self.graph.edges['bi_to'], [('bi_from', 1)])
        self.graph.add_edge('from', 'to', bidirectional=False)
        self.assertEqual(self.graph.edges['from'], [('to', 1)])
        with self.assertRaises(KeyError):
            self.assertEqual(self.graph.edges['to'], [])

        self.graph.add_edge('weight_from', 'weight_to', weight=5)
        self.assertEqual(self.graph.edges['weight_from'], [('weight_to', 5)])
        self.graph.add_edge('weight_bi_from', 'weight_bi_to', bidirectional=True, weight=5)
        self.assertEqual(self.graph.edges['weight_bi_from'], [('weight_bi_to', 5)])
        self.assertEqual(self.graph.edges['weight_bi_to'], [('weight_bi_from', 5)])

    def test_remove_edge(self):
        self.assertEqual(len(self.graph.edges), 0)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.assertEqual(len(self.graph.edges[1]), 2)
        self.graph.remove_edge(1, 2)
        self.assertEqual(len(self.graph.edges[1]), 1)
        self.assertEqual(self.graph.edges[1], [(3, 1)])

        with self.assertRaises(ValueError):
            self.graph.remove_edge(1, 2)


if __name__ == "__main__":
    unittest.main()



