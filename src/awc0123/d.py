import heapq


def topological_sort(graph):
    n = len(graph)
    indeg = [0] * n

    for v in range(n):
        for to in graph[v]:
            indeg[to] += 1

    q = [v for v in range(n) if indeg[v] == 0]
    heapq.heapify(q)
    order = []

    while len(q):
        v = heapq.heappop(q)
        order.append(v)

        for to in graph[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                heapq.heappush(q, to)
    return order if len(order) == n else []


N, M = map(int, input().split())

graph = [[] for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)


res = topological_sort(graph)

if len(res) == 0:
    print(-1)
else:
    print(*[r + 1 for r in res])
