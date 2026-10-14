from heapq import heappop, heappush


N, M, K = map(int, input().split())
graph = [[] for i in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))


dist = [float("inf") for i in range(N)]
dist[0] = 0
queue = [(0, 0)]
while queue:
    cost, v = heappop(queue)
    if cost != dist[v]:
        continue
    for u, c in graph[v]:
        if dist[u] > dist[v] + c:
            dist[u] = dist[v] + c
            heappush(queue, (dist[u], u))

print(-1 if dist[N - 1] > K else dist[N - 1])
