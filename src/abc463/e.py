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


N, M, Y = map(int, input().split())

# 0~N-1: 都市の頂点
# N: ワープゲート
# i -> N: Xi+Y
# N -> j: Xj
graph = [[] for i in range(N + 1)]


for _ in range(M):
    u, v, T = map(int, input().split())
    u, v = u - 1, v - 1
    graph[u].append((v, T))
    graph[v].append((u, T))

X = list(map(int, input().split()))

for i in range(N):
    graph[i].append((N, X[i] + Y))
    graph[N].append((i, X[i]))

dist = dijkstra(0, graph)


ans = []
for i in range(1, N):
    ans.append(dist[i])

print(*ans)
