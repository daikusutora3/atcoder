from collections import deque


N, M, K = map(int, input().split())
S = list(map(int, input().split()))
graph = [[] for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)

queue = deque([s - 1 for s in S])
ans = [0 for i in range(N)]
for s in S:
    ans[s - 1] = 1

while len(queue):
    v = queue.popleft()
    for u in graph[v]:
        if not ans[u]:
            ans[u] = 1
            queue.append(u)

print(sum(ans))
