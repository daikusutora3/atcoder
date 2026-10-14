from atcoder.maxflow import MFGraph

V, E = map(int, input().split())
g = MFGraph(V)
for _ in range(E):
    u, v, c = map(int, input().split())
    g.add_edge(u - 1, v - 1, c)

print(g.flow(0, V - 1))
