from itertools import combinations


N, M, K = map(int, input().split())
A = list(map(int, input().split()))
graph = [[0 for j in range(N)] for i in range(N)]

for _ in range(M):
    u, v, b = map(int, input().split())
    graph[v - 1][u - 1] = -b
    graph[u - 1][v - 1] = -b

ans = -float("inf")
for com in combinations(range(N), K):
    res = 0
    for member in com:
        res += A[member]
    for i in range(K):
        member1 = com[i]
        for j in range(i + 1, K):
            member2 = com[j]
            res += graph[member1][member2]
    ans = max(ans, res)

print(ans)
