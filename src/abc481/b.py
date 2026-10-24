N, K = map(int, input().split())

A = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    Al, Ar = A[i], A[i - 1]
    if Al <= K <= Ar or Ar <= K <= Al:
        ans += 1

for i in range(1, N - 1):
    if A[i] == K:
        ans -= 1

print(ans)
