N = int(input())
S = input()
mod = 10**9 + 7

dp = [[0 for j in range(i + 1)] for i in range(N)]
dp[0][0] = 1

for i in range(N - 1):
    rui = [0 for j in range(i + 2)]
    for j in range(i + 1):
        rui[j + 1] += rui[j] + dp[i][j]
        rui[j + 1] %= mod

    for j in range(i + 2):
        if S[i] == "<":
            dp[i + 1][j] += rui[j]
        else:
            dp[i + 1][j] += rui[i + 1] - rui[j]
        dp[i + 1][j] %= mod

print(sum(dp[N - 1]) % mod)
