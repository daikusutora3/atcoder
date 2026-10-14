from collections import deque


N, M, Q = map(int, input().split())

graph = [[] for i in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)

ans = [0 for i in range(N + 1)]

for s in range(N):
    dist = [-1 for i in range(N)]
    dist[s] = 0
    queue = deque([s])
    while queue:
        v = queue.popleft()
        for nv in graph[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            queue.append(nv)
    # print(s, dist)
    if -1 in dist:
        continue
    else:
        ans[max(dist)] += 1

for i in range(N):
    ans[i + 1] += ans[i]

for _ in range(Q):
    K = int(input())
    print(ans[K])
