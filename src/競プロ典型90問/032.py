from itertools import permutations


N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
M = int(input())
graph = [set() for i in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x - 1].add(y - 1)
    graph[y - 1].add(x - 1)
ans = float("inf")
for p in permutations(range(N), N):
    owari = False
    for i in range(N - 1):
        # iとi+1の人の相性を確認
        if p[i + 1] in graph[p[i]]:
            owari = True
    if owari:
        continue
    res = 0
    for i in range(N):
        res += A[p[i]][i]
    ans = min(ans, res)

print(ans if ans != float("inf") else -1)
