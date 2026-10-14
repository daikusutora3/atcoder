import math

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

ans = []
for i in range(N):
    rigai_num = len(graph[i])
    ans.append(math.comb(N - rigai_num - 1, 3))

print(*ans)
