N, M = map(int, input().split())
A = list(map(int, input().split()))

imos = [0 for i in range(N + 1)]

for _ in range(M):
    L, R, D = map(int, input().split())
    imos[L - 1] += D
    imos[R] -= D

for i in range(N):
    imos[i + 1] += imos[i]

ans = []

for i in range(N):
    ans.append(A[i] + imos[i])
print(*ans)
