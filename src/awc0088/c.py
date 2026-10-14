N, M = map(int, input().split())

A = list(map(int, input().split()))

imos = [0 for i in range(N + 1)]

for _ in range(M):
    L, R = map(int, input().split())
    imos[L - 1] += 1
    imos[R] -= 1

for i in range(N):
    imos[i + 1] += imos[i]

ans = 0

for i in range(N):
    if imos[i] > 0:
        ans += A[i]

print(ans)
