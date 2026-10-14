from atcoder.maxflow import MFGraph

N = int(input())
a = list(map(int, input().split()))

# 0~N-1: 各宝石の頂点
# N: 始点S
# N+1: 終点T
graph = MFGraph(N + 2)

for i in range(N):
    for j in range(2 * i + 1, N, i + 1):
        graph.add_edge(i, j, float("inf"))


ans = 0
for i in range(N):
    if a[i] >= 0:
        graph.add_edge(i, N + 1, a[i])
        ans += a[i]
    else:
        graph.add_edge(N, i, -a[i])

ans -= graph.flow(N, N + 1)
print(ans)
