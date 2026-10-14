from atcoder.maxflow import MFGraph

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(M)]
c = list(map(int, input().split()))
# 0: 流しはじめの頂点
# 2*i-1, 2*i: i番目(0-index)の２頂点分割における頂点番号の割り振り
# 2*i-1 -> 2*i
# 2*N-3: 流し終わりの頂点
g = MFGraph(2 * N - 2)

for a, b in ab:
    if a > b:
        a, b = b, a
    a -= 1
    b -= 1
    # aが始点
    if a == 0:
        # print(f"{0}->{2 * b - 1}: {float('inf')}")
        g.add_edge(0, 2 * b - 1, float("inf"))
    # bが終点
    elif b == N - 1:
        # print(f"{2 * a}->{2 * N - 3}: {float('inf')}")
        g.add_edge(2 * a, 2 * N - 3, float("inf"))
    # aとbは始点でも終点でもない
    else:
        # print(f"{2 * a}<->{2 * b - 1}: {float('inf')}")
        # print(f"{2 * b}<->{2 * a - 1}: {float('inf')}")
        g.add_edge(2 * a, 2 * b - 1, float("inf"))
        g.add_edge(2 * b, 2 * a - 1, float("inf"))

for i in range(1, N - 1):
    # print(f"{2 * i - 1}->{2 * i}: {c[i]}")
    g.add_edge(2 * i - 1, 2 * i, c[i])

print(g.flow(0, 2 * N - 3))
visited = g.min_cut(0)
ans = set()
for edge in g.edges():
    if (
        visited[edge.src]
        and (not visited[edge.dst])
        and edge.flow > 0
        and edge.cap < float("inf")
    ):
        ans.add(edge.dst // 2 + 1)

ans = sorted(ans)
print(len(ans))
print(*ans)
