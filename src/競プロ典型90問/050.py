N, L = map(int, input().split())
dp = [0 for i in range(N + 1)]
mod = 10**9 + 7
dp[0] = 1
cnt = 1
for i in range(1, N + 1):
    dp[i] = (dp[i - 1] + (dp[i - L] if i - L >= 0 else 0)) % mod

print(dp[N])
