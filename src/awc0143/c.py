from collections import deque

N, M = map(int, input().split())
C = list(map(int, input().split()))

graph = [[] for i in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if C[u] == C[v]:
        continue
    graph[u].append(v)

seen = [False for i in range(N)]
seen[0] = True
queue = deque([0])
while len(queue):
    v = queue.popleft()
    for nv in graph[v]:
        if seen[nv]:
            continue
        seen[nv] = True
        queue.append(nv)

ans = []

for i in range(N):
    if not seen[i]:
        ans.append(i + 1)


if len(ans):
    print(*ans)
else:
    print("COMPLETE")
