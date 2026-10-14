from atcoder.maxflow import MFGraph

N = int(input())

# 0~N-1: アイテム
# N~2*N-1: ボール
# 2*N: Source
# 2*N+1: Target

graph = MFGraph(2 * N + 2)
# Source to Item
for i in range(N):
    graph.add_edge(2 * N, i, 1)

# Item to ball
for i in range(N):
    A, B = map(int, input().split())
    graph.add_edge(i, N + A - 1, 1)
    graph.add_edge(i, N + B - 1, 1)

# ball to Target
for i in range(N):
    graph.add_edge(N + i, 2 * N + 1, 1)

num = graph.flow(2 * N, 2 * N + 1)
print(N, len(graph.edges()))
for e in graph.edges():
    print(e.src, e.dst)

print(num)
