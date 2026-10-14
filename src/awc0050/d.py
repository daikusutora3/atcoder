import heapq

N, M, K = map(int, input().split())
graph = [[] for i in range(N)]
for i in range(M):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

ryoukin = [0 for i in range(N)]
for _ in range(K):
    L, C = map(int, input().split())
    ryoukin[L - 1] = C

INF = float("inf")


def dijkstra(s, graph):
    global INF, ryoukin
    dist = [INF for i in range(len(graph))]
    dist[s] = 0
    queue = [(0, s)]
    while queue:
        cost, v = heapq.heappop(queue)
        if cost != dist[v]:
            continue
        for u, c in graph[v]:
            if dist[u] > dist[v] + c + ryoukin[u]:
                dist[u] = dist[v] + c + ryoukin[u]
                heapq.heappush(queue, (dist[u], u))
    return dist


dist = dijkstra(0, graph)
print(dist[N - 1] + ryoukin[0])
