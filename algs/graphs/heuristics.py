def manhattan(start, end):
    """
    a simple minimum cost boundary heuristic using manhattan shortest path
    """
    (x1, y1) = start
    (x2, y2) = end
    return abs(x1-x2) + abs(y1-y2)
