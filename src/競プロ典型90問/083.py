from math import isqrt


N, M = map(int, input().split())
graph = [[] for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

K = isqrt(N)
s = set()
for i in range(N):
    if len(graph[i]) > K:
        s.add(i)

# Kgraphの隣接リストのサイズはO(√N)
Kgraph = [[] for i in range(N)]
# [color, time]
lazy_ct = [-1 for i in range(N)]
ct = [[1, -1] for i in range(N)]

for i in range(N):
    for j in graph[i]:
        if j in s:
            Kgraph[i].append(j)

# print("K:", K)
ans = []
Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    x = x - 1
    color = ct[x][0]
    time = ct[x][1]
    for v in Kgraph[x]:
        if lazy_ct[v] != -1 and time < lazy_ct[v][1]:
            color, time = lazy_ct[v]
    ans.append(color)
    ct[x] = [y, _]
    if x not in s:
        for v in graph[x]:
            ct[v] = [y, _]
    else:
        lazy_ct[x] = [y, _]
        for v in Kgraph[x]:
            ct[v] = [y, _]

print(*ans, sep="\n")
