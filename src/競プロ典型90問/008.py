N = int(input())
S = input()
mod = 10**9 + 7
l = ["", "a", "t", "c", "o", "d", "e", "r"]
dp = [[0 for k in l] for i in range(N + 1)]

dp[0][0] = 1

for i in range(1, N + 1):
    for k in range(len(l)):
        if S[i - 1] == l[k]:
            dp[i][k] = dp[i - 1][k] + dp[i - 1][k - 1]
        else:
            dp[i][k] = dp[i - 1][k]
        dp[i][k] %= mod

print(dp[N][len(l) - 1])
