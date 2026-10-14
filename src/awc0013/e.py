from atcoder.maxflow import MFGraph

N, M = map(int, input().split())
C = [list(map(int, input().split()))[1:] for i in range(N)]

# 0~N+M-1: 人と時間帯に対して頂点を割り振る
# N+M: startの頂点
# N+M+1: endの頂点
graph = MFGraph(N + M + 2)

for time in range(N):
    for c in C[time]:
        graph.add_edge(c - 1, time + M, 1)

for i in range(M):
    graph.add_edge(N + M, i, 1)

for time in range(N):
    graph.add_edge(time + M, N + M + 1, 1)

ans = graph.flow(N + M, N + M + 1)
print(ans)

# pprint(graph.edges())
