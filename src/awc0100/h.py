from collections import deque


N, M = map(int, input().split())
graph = [[] for i in range(N)]
B = list(map(int, input().split()))
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    graph[u].append(v)

for v in range(N):
    graph[v].sort(key=lambda x: -B[x])
    graph[v] = deque(graph[v])


ans = []
seen = [False for _ in range(N)]
queries = list(range(1, N))
queries.sort(key=lambda x: -B[x])
queries = [0] + queries


for i in queries:
    if seen[i]:
        continue
    queue = deque([i])
    ans.append(i + 1)
    seen[i] = True
    while len(queue):
        v = queue.popleft()
        while len(graph[v]):
            nv = graph[v].popleft()
            if not seen[nv]:
                seen[nv] = True
                queue.append(nv)
                ans.append(nv + 1)
                break


print(*ans)
