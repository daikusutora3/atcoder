import sys

sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


dp = [0 for i in range(N)]


def dfs(v, p):
    cnt = 1
    for u in graph[v]:
        # print(f"{u} -> {v}: {graph[v]}, {p}")
        if p == u:
            continue
        cnt += dfs(u, v)
    dp[v] = cnt * (N - cnt)
    return cnt


dfs(0, -1)

print(sum(dp))
