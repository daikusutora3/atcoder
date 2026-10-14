N, M = map(int, input().split())
graph = [[] for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

ans = 0
for v in range(N):
    cnt = 0
    for u in graph[v]:
        if u < v:
            cnt += 1
    if cnt == 1:
        ans += 1

print(ans)
