import sys

sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
V = list(map(int, input().split()))
P = list(map(int, input().split()))
graph = [[] for i in range(N)]
for i in range(N - 1):
    graph[P[i] - 1].append(i + 1)

isan = [0 for i in range(N)]
isan[0] = V[0]


def dfs(v):
    global isan
    for u in graph[v]:
        isan[u] += isan[v] + V[u]
        # print(f"{v} -> {u}: {isan}")
        dfs(u)


dfs(0)

# print(isan)
for _ in range(Q):
    x = int(input())
    print(isan[x - 1])
