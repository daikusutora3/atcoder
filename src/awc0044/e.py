N, M = map(int, input().split())
D = list(map(int, input().split()))
dp = [[0 for j in range(min(N, M) + 1)] for i in range(N + 1)]
dp[0][0] = 1
MOD = 998244353
for i in range(N):
    for j in range(min(N, M) + 1):
        if D[i] == 0:
            dp[i + 1][j] += dp[i][j] * j
            dp[i + 1][j] %= MOD
            if j - 1 >= 0 and M - j + 1 > 0:
                dp[i + 1][j] += dp[i][j - 1] * (M - j + 1)
                dp[i + 1][j] %= MOD
        elif D[i] <= j:
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
            if D[i] == j and M - j + 1 > 0:
                dp[i + 1][j] += dp[i][j - 1] * (M - j + 1)
                dp[i + 1][j] %= MOD

ans = 0
for a in dp[N]:
    ans = (ans + a) % MOD
print(ans)
