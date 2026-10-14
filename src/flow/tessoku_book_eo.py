from atcoder.maxflow import MFGraph

N, M = map(int, input().split())
P = list(map(int, input().split()))

# 0~N-1: 各駅の頂点
# N: 始点S
# N+1: 終点T
graph = MFGraph(N + 2)

for _ in range(M):
    A, B = map(int, input().split())
    graph.add_edge(A - 1, B - 1, float("inf"))

ans = 0
for i in range(N):
    if P[i] >= 0:
        # print(f"始点 -> {i}: {P[i]}")
        graph.add_edge(N, i, P[i])
        ans += P[i]
    else:
        # print(f"{i} -> 終点: {-P[i]}")
        graph.add_edge(i, N + 1, abs(P[i]))

print(ans - graph.flow(N, N + 1))
