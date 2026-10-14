from collections import defaultdict

from atcoder.maxflow import MFGraph

N, T = map(int, input().split())
AXY = [tuple(map(int, input().split())) for i in range(N)]
BXY = [tuple(map(int, input().split())) for i in range(N)]
d_BXY = defaultdict(list)
for j in range(N):
    d_BXY[BXY[j]].append(j)

# 0~N-1: startとなるA側の頂点
# N~2*N-1: endとなるB側の頂点
# 2*N: Sの頂点
# 2*N+1: Tの頂点
graph = MFGraph(2 * N + 2)

direction = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
# A -> Bに対しての辺を構築
for i in range(N):
    ax, ay = AXY[i]
    for dx, dy in direction:
        bx = ax + dx * T
        by = ay + dy * T
        if (bx, by) in d_BXY:
            for j in d_BXY[(bx, by)]:
                graph.add_edge(i, j + N, 1)

# S -> Aに対しての辺を構築
for i in range(N):
    graph.add_edge(2 * N, i, 1)

# B -> Tに対しての辺を構築
for j in range(N):
    graph.add_edge(j + N, 2 * N + 1, 1)


flow = graph.flow(2 * N, 2 * N + 1)
ans = [-1 for i in range(N)]
for e in graph.edges():
    if 0 <= e.src < N and N <= e.dst < 2 * N and e.flow == 1:
        i = e.src
        j = e.dst - N
        ax, ay = AXY[i]
        for d, (dx, dy) in enumerate(direction):
            if (ax + dx * T, ay + dy * T) == BXY[j]:
                ans[i] = d + 1


if flow == N:
    print("Yes")
    print(*ans)
else:
    print("No")
