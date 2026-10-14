import heapq


N, M, S, T = map(int, input().split())

# 0~N-1: バス停頂点
# N~N+M-1: バス頂点
graph = [[] for i in range(N + M)]


for i in range(M):
    A = list(map(int, input().split()))[1:]
    for a in A:
        graph[a - 1].append((N + i, 1))
        graph[N + i].append((a - 1, 0))

INF = float("inf")


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


dist = dijkstra(S - 1, graph)

print(dist[T - 1] if dist[T - 1] != INF else -1)
