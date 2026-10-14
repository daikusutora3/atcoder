import itertools


N, M = map(int, input().split())
A = list(map(int, input().split()))
UV = [list(map(int, input().split())) for i in range(M)]

ans = 0

for perm in itertools.permutations([i + 1 for i in range(N)]):
    flag = False
    for u, v in UV:
        if not (perm[u - 1] < perm[v - 1]):
            flag = True
    if flag:
        continue
    res = 0
    for i in range(N):
        res += perm[i] * A[i]
    ans = max(ans, res)


print(ans)
