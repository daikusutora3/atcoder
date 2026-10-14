from collections import deque


N, M, K, T = map(int, input().split())
C = list(map(int, input().split()))
graph = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

queue = deque([])
uwasa = [False for i in range(N)]
cnt = [0 for i in range(N)]
for c in C:
    queue.append(c - 1)
    uwasa[c - 1] = True
    for u in graph[c - 1]:
        cnt[u] += 1

while queue:
    v = queue.popleft()
    for u in graph[v]:
        if not uwasa[u] and cnt[u] >= T:
            queue.append(u)
            uwasa[u] = True
            for a in graph[u]:
                cnt[a] += 1

print(sum(uwasa))
