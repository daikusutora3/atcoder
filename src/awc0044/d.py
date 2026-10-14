import heapq

INF = 2**64


N, M, K = map(int, input().split())
UVM = [list(map(int, input().split())) for i in range(M)]
C = set(map(int, input().split())) if K > 0 else set()
graph = [[] for i in range(N)]

for i in range(M):
    u, v, w = UVM[i]
    graph[u - 1].append([v - 1, 2 * w if i + 1 in C else w])
    graph[v - 1].append([u - 1, 2 * w if i + 1 in C else w])


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


dist = dijkstra(0, graph)
print(-1 if dist[N - 1] == INF else dist[N - 1])
