from atcoder.maxflow import MFGraph

N, G, E = map(int, input().split())
P = list(map(int, input().split()))
g = MFGraph(N + 1)

for _ in range(E):
    a, b = map(int, input().split())
    g.add_edge(a, b, 1)
    g.add_edge(b, a, 1)

for p in P:
    g.add_edge(p, N, 1)

print(g.flow(0, N))
