import sys


sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

# 塗ってる: 1
# 塗ってない: 0
paint = [0 for i in range(N)]


def dfs(v, p):
    global paint
    is_paintable = True
    for u in graph[v]:
        if u == p:
            continue
        dfs(u, v)
        if paint[u]:
            is_paintable = False

    if is_paintable:
        paint[v] = 1
    return


dfs(0, -1)

cnt = N // 2
for i in range(N):
    if paint[i]:
        print(i + 1)
        cnt -= 1
    if cnt <= 0:
        break
