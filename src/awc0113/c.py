from collections import deque


N, M, K, Q, T = map(int, input().split())
UV = [] if M == 0 else [list(map(int, input().split())) for _ in range(M)]
S = list(map(int, input().split()))
P = set() if Q == 0 else set(map(int, input().split()))


graph = [[] for i in range(N)]
for u, v in UV:
    if u in P or v in P:
        continue
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

dist = [float("inf") for _ in range(N)]
queue = deque([T - 1])
dist[T - 1] = 0
while len(queue):
    v = queue.popleft()
    for nv in graph[v]:
        if dist[nv] == float("inf"):
            dist[nv] = dist[v] + 1
            queue.append(nv)

ans = -float("inf")

# print(dist)
for s in S:
    ans = max(ans, dist[s - 1])

print(-1 if ans == float("inf") else ans)
