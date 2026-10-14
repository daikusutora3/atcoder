from atcoder.maxflow import MFGraph

N, M = map(int, input().split())
B = list(map(int, input().split()))

# 0~N-1: 参加者頂点
# N~N+M-1: プレンゼント頂点
# N+M: 始点
# N+M+1: 終点
g = MFGraph(N + M + 2)

# 始点 -> 参加者頂点
for i in range(N):
    g.add_edge(N + M, i, 1)

# プレンゼント頂点 -> 終点
for i in range(M):
    g.add_edge(N + i, N + M + 1, B[i])

for i in range(N):
    C = list(map(int, input().split()))
    for j in range(1, C[0] + 1):
        g.add_edge(i, N + C[j] - 1, 1)

print(g.flow(N + M, N + M + 1))
