from heapq import heappop, heappush


def dijkstra(s, graph, inf=float("inf")):
    """計算量: 時間 O(V + E log(E + 2))、追加空間 O(V + E)。V は頂点数、E は辺数。重みは非負。

    Source: https://github.com/daikusutora3/atcoder
    """
    dist = [inf] * len(graph)
    dist[s] = 0
    que = [(0, s)]

    while que:
        cost, v = heappop(que)

        if cost != dist[v]:
            continue

        for to, w in graph[v]:
            nd = cost + w

            if nd < dist[to]:
                dist[to] = nd
                heappush(que, (nd, to))

    return dist


N, M, S, T = map(int, input().split())

graph = [[] for i in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)

for i in range(N):
    graph[i].sort()

g = [[] for i in range(N)]

for i in range(N):
    if len(graph[i]):
        g[i].append((graph[i][0], 0))
    for j in range(1, len(graph[i])):
        g[i].append((graph[i][j], 1))


dist = dijkstra(S - 1, g)
if dist[T - 1] == float("inf"):
    print(-1)
else:
    print(dist[T - 1])
