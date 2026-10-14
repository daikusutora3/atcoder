from collections import defaultdict


N, M = map(int, input().split())
graph = [[] for i in range(M)]
RC = [list(map(int, input().split())) for _ in range(M)]

d = defaultdict(lambda: -1)

for i, (r, _) in enumerate(RC):
    if d[r] != -1:
        graph[d[r]].append(i)
    d[r] = i

d = defaultdict(lambda: -1)

for i, (_, c) in enumerate(RC):
    if d[c] != -1:
        graph[d[c]].append(i)
    d[c] = i

ans = 0

for i in range(M):
    if len(graph[i]) == 0:
        ans += 1

print(ans)
