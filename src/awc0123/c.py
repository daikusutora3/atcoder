import sys

sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int, input().split()))
P = list(map(int, input().split()))
B = list(map(int, input().split()))

graph = [[] for i in range(N)]

for i in range(N - 1):
    graph[P[i] - 1].append(i + 1)


# 頂点vを根とする部分木T_vに対する: (人の合計人数, ans)
def dfs(v, s):
    res = s * B[v]
    for nv in graph[v]:
        res += dfs(nv, s + A[nv])
    return res


print(dfs(0, A[0]) - A[0] * B[0])
