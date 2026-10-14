import sys


sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int, input().split()))
graph = [[] for i in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

ans = [False for i in range(N)]


def dfs(v, p, s: set):
    global graph, ans
    flag = True
    if p != -1:
        ans[v] |= ans[p]
    if A[v] in s:
        flag = False
        ans[v] = True
    s.add(A[v])
    for u in graph[v]:
        if u == p:
            continue
        dfs(u, v, s)
    if flag:
        s.remove(A[v])


dfs(0, -1, set())

for i in range(N):
    print("Yes" if ans[i] else "No")
