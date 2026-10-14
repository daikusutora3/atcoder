from heapq import heappop, heappush


def dijkstra(s, graph, inf=float("inf")):
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


N, M, K = map(int, input().split())

g = [[] for i in range(N)]
UV = [list(map(int, input().split())) for i in range(M)]
for _ in range(M):
    u, v = UV[_]
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

konzatu = set()
for i in range(N):
    if len(g[i]) >= K:
        konzatu.add(i)

graph = [[] for i in range(N)]
for _ in range(M):
    u, v = UV[_]

    graph[u - 1].append((v - 1, 2 if (v - 1) in konzatu else 1))
    graph[v - 1].append((u - 1, 2 if (u - 1) in konzatu else 1))

dist = dijkstra(0, graph)
print(
    -1
    if dist[N - 1] == float("inf")
    else (dist[N - 1] - (1 if N - 1 in konzatu else 0))
)
