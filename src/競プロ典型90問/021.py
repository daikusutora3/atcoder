from atcoder.scc import SCCGraph

N, M = map(int, input().split())

graph = SCCGraph(N)

for i in range(M):
    a, b = map(int, input().split())
    graph.add_edge(a - 1, b - 1)

scc = graph.scc()

ans = 0
for group in scc:
    # print(group, len(group))
    ans += (len(group) * (len(group) - 1)) // 2

print(ans)
