from atcoder.maxflow import MFGraph

N = int(input())
C = [input() for i in range(N)]

# 0~N-1: 生徒頂点
# N~2*N-1: 席頂点
# 2*N: 始点
# 2*N+1: 終点
g = MFGraph(2 * N + 2)

# 始点 -> 生徒頂点
for i in range(N):
    g.add_edge(2 * N, i, 1)

# 席頂点 -> 終点
for i in range(N):
    g.add_edge(i + N, 2 * N + 1, 1)

for i in range(N):
    for j in range(N):
        if C[i][j] == "#":
            g.add_edge(i, j + N, 1)

print(g.flow(2 * N, 2 * N + 1))
