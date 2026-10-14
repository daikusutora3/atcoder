N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(key=lambda x: x % K)
ans = float("inf")
ans = min(ans, A[-1] % K - A[0] % K)
for i in range(N):
    a = A[i]
    if i > 0:
        ans = min(ans, A[i - 1] % K + (K - A[i] % K))
    if i < N - 1:
        ans = min(ans, A[i] % K + (K - A[i + 1] % K))

print(ans)
