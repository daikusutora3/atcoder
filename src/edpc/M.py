N, K = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0 for k in range(K + 1)] for i in range(N + 1)]
dp[0][0] = 1
mod = 10**9 + 7

for i in range(N):
    rui = [0 for k in range(K + 2)]
    for j in range(K + 1):
        rui[j + 1] += rui[j] + dp[i][j]
        rui[j + 1] %= mod
    for j in range(K + 1):
        dp[i + 1][j] += rui[j + 1] - rui[max(0, j - a[i])]
        dp[i + 1][j] %= mod

print(dp[N][K])
