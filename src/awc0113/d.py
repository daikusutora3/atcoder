N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [-float("inf") for _ in range(N + 1)]
dp[0] = 0
for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1] + A[i - 1])
    if i - K >= 0:
        dp[i] = max(dp[i], dp[i - K])

print(dp[N])
