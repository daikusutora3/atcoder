N, M = map(int, input().split())
graph = [set() for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].add(b - 1)


ans = 0
for i in range(N):
    for j in graph[i]:
        if i in graph[j]:
            ans += 1

print(ans // 2)
