from collections import deque


def topological_sort(graph):
    n = len(graph)
    indeg = [0] * n

    for v in range(n):
        for to in graph[v]:
            indeg[to] += 1

    q = deque(v for v in range(n) if indeg[v] == 0)
    order = []

    while q:
        v = q.popleft()
        order.append(v)

        for to in graph[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)

    return order if len(order) == n else []
