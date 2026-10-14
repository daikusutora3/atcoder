import sys
from collections import deque

from atcoder.maxflow import MFGraph

input = sys.stdin.buffer.readline

N, M = map(int, input().split())

g = [[] for i in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    g[u].append(v)
    g[v].append(u)

colors = [-1 for i in range(N)]


def bfs(v):
    global colors, g
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for nv in g[v]:
            if colors[nv] == -1:
                colors[nv] = (colors[v] + 1) % 2
                queue.append(nv)


for i in range(N):
    if colors[i] == -1:
        colors[i] = 0
        bfs(i)

# 0~N-1: 建物頂点
# N: 始点
# N+1: 終点
graph = MFGraph(N + 2)

for i in range(N):
    if colors[i] == 1:
        graph.add_edge(N, i, 1)
    else:
        graph.add_edge(i, N + 1, 1)
    if colors[i] == 0:
        continue
    for j in g[i]:
        graph.add_edge(i, j, 1)

print(graph.flow(N, N + 1))
