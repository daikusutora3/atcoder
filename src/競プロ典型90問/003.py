import sys

sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

dist = [-1 for i in range(N)]
dist[0] = 0
max_dist = {"dist": 0, "node": 0}


def dfs(v, prev):
    global dist, max_dist
    for u in graph[v]:
        if u == prev:
            continue
        dist[u] = dist[v] + 1
        if max_dist["dist"] < dist[u]:
            max_dist = {"dist": dist[u], "node": u}
        dfs(u, v)
    return


dfs(0, 0)

dist = [-1 for i in range(N)]
dist[max_dist["node"]] = 0
max_dist = {"dist": 0, "node": max_dist["node"]}

dfs(max_dist["node"], max_dist["node"])

print(max_dist["dist"] + 1)
