import heapq


N, M, K = map(int, input().split())

INF = float("inf")

graph = [[] for i in range(N)]

for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u - 1].append([v - 1, c])
    graph[v - 1].append([u - 1, c])


def dijkstra(s, graph):
    global INF
    dist = [INF for i in range(len(graph))]
    dist[s] = 0
    queue = [(0, s)]
    while queue:
        cost, v = heapq.heappop(queue)
        if cost != dist[v]:
            continue
        for u, c in graph[v]:
            if dist[u] > dist[v] + c:
                dist[u] = dist[v] + c
                heapq.heappush(queue, (dist[u], u))
    return dist


dist = dijkstra(K - 1, graph)
ans = dist[0] + dist[N - 1]
print(-1 if ans == INF else ans)
