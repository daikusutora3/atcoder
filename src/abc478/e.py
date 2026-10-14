from atcoder.scc import SCCGraph
import sys

N, Q = map(int, input().split())
tuv = [list(map(int, input().split())) for i in range(Q)]
graph = SCCGraph(N)
for _ in range(Q):
    t, u, v = tuv[_]
    graph.add_edge(v - 1, u - 1)

scc = graph.scc()

id = [0 for i in range(N)]
for i, group in enumerate(scc):
    for v in group:
        id[v] = i
for t, u, v in tuv:
    if t == 1 and id[u - 1] == id[v - 1]:
        print("No")
        sys.exit()

print(scc)
now = N
ans = [0 for i in range(N)]
for group in scc:
    for v in group:
        ans[v] = now
    now -= 1

print("Yes")
print(*ans)

# for t, u, v in tuv:
#     if t == 1:
#         if ans[u - 1] < ans[v - 1]:
#             print("OK")
#         else:
#             print("No")
#     if t == 0:
#         if ans[u - 1] <= ans[v - 1]:
#             print("OK")
#         else:
#             print("No")
