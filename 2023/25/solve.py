from algas.input import tokens_split
from algas.aoc.aoc import part1
from itertools import combinations
import networkx as nx


@part1()
def solve():
    graph = nx.Graph()
    for source, dests in tokens_split(splitter=': '):
        for dest in dests.split(' '):
            graph.add_edge(source, dest, capacity=1.0)

    for n, m in combinations(graph.nodes, 2):
        cuts, partitions = nx.minimum_cut(graph, n, m)
        if cuts == 3:
            return len(partitions[0])*len(partitions[1])


if __name__ == '__main__':
    pass
