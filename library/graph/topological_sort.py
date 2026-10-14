from collections import deque


def topological_sort(graph):
    """計算量: 時間 O(V + E)、追加空間 O(V)。V は頂点数、E は辺数。

    Source: https://github.com/daikusutora3/atcoder
    """
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
