import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for i in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    graph[y].append(x)


dist = [-1 for i in range(N)]


def dfs(v):
    global graph, dist
    if len(graph[v]) == 0:
        return 0
    if dist[v] != -1:
        return dist[v]
    res = 0
    for nv in graph[v]:
        res = max(res, dfs(nv) + 1)
    dist[v] = res
    return res


for i in range(N):
    dfs(i)

print(max(dist))
