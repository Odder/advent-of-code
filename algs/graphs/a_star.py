from algas.graphs.graph import PriorityQueue
from algas.graphs.heuristics import manhattan


def a_star(graph, start, goal, heuristic=manhattan, bidirectional=False):
    """
    a* algorithm
    """

    # Initialise priority queue
    queue = PriorityQueue()
    queue.append(start, 0)

    # Initialise trailing
    came_from = {
        start: 0
    }
    # Initialise weights of all nodes
    costs = {
        start: 0
    }

    if bidirectional:
        # Initialise priority queue
        queue2 = PriorityQueue()
        queue2.append(goal, 0)

        # Initialise trailing
        came_from2 = {
            goal: 0
        }
        # Initialise weights of all nodes
        costs2 = {
            goal: 0
        }

        # Statistics
    nodes_visited = 0

    # As long as there are nodes to visit, let's visit!
    while not queue.empty():

        # Get the next item from the queue
        current = queue.pop()

        nodes_visited += 1

        # We are done!
        if not bidirectional and current == goal \
                or bidirectional and current in costs2:

            if bidirectional:
                total_cost = costs[current] + costs2[current]
            else:
                total_cost = costs[goal]

            # Backtrack the route for output
            route = []
            c = current
            while c:
                route.append(c)
                c = came_from[c]

            if bidirectional:
                while current:
                    route.append(current)
                    current = came_from2[current]

            # Reverse the route
            route = route[::-1]

            # Return a nice object with the route and length
            return route, total_cost, nodes_visited

        # Append all neighbouring nodes to the queue
        for (next, cost) in graph.neighbours(current):

            # Apply cost to new node (grid -> +1)
            new_cost = costs[current] + cost

            # If node is not already in the queue, or the current registered cost is
            # higher, we need to set/update the cost for that node
            if next not in costs or new_cost < costs[next]:
                # Update cost
                costs[next] = new_cost

                # Add heuristics
                priority = new_cost + heuristic(goal, next)

                # Append to queue
                queue.append(next, priority)

                # Append to trail
                came_from[next] = current

        if bidirectional:
            # Get the next item from the queue
            current = queue2.pop()

            nodes_visited += 1

            # Append all neighbouring nodes to the queue
            for (next, cost) in graph.neighbours(current):

                # Apply cost to new node (grid -> +1)
                new_cost = costs2[current] + cost

                # If node is not already in the queue, or the current registered cost is
                # higher, we need to set/update the cost for that node
                if next not in costs2 or new_cost < costs2[next]:
                    # Update cost
                    costs2[next] = new_cost

                    # Add heuristics
                    priority = new_cost + heuristic(start, next)

                    # Append to queue
                    queue2.append(next, priority)

                    # Append to trail
                    came_from2[next] = current

    # We only reach this part if no path was found
    raise Exception('no path found')