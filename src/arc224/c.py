import sys

sys.setrecursionlimit(10**6)


ans = []
now = 0


def solve():
    global ans, now
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    ans = [-1 for i in range(N)]

    def dfs(v, p):
        global ans, now
        ans[v] = ans[p] + 1
        for nv in graph[v]:
            if nv == p or ans[nv] != -1:
                continue
            dfs(nv, v)

    dfs(0, -1)
    print(*ans)


T = int(input())
for _ in range(T):
    solve()
