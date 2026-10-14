import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
P = list(map(int, input().split()))
graph = [[] for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    if P[u - 1] < P[v - 1]:
        graph[u - 1].append(v - 1)


result = [-1 for i in range(N)]


def dfs(v):
    global result
    if result[v] != -1:
        return result[v]
    res = 0
    for nv in graph[v]:
        res = max(res, dfs(nv))
    result[v] = res + 1
    return result[v]


print(dfs(0))


# print(graph)
# P = [(p, i) for i, p in enumerate(P)]
# P = sorted(P)
# d = defaultdict(lambda: 1)

# for p, u in P:
#     for v in graph[u]:
#         d[v] = max(d[v], d[u] + 1)

# print(max(d.values()) if len(d.values()) > 0 else 1)
