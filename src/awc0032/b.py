N, K, M = map(int, input().split())

A = list(map(int, input().split()))
ans = 0

for i in range(N):
    ans += (A[i] // (K + M)) + (0 if A[i] % (K + M) == 0 else 1)

print(ans)
