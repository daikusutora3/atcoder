S = input()
mod = 998244353
dp = [[0 for c in range(4)] for i in range(len(S) + 1)]
dp[0][0] = 1
d = {"a": 1, "b": 2, "c": 3}
for i, s in enumerate(S):
    sum_dp_i = sum(dp[i])
    for c in range(4):
        dp[i + 1][c] += dp[i][c]
        dp[i + 1][c] %= mod
    dp[i + 1][d[s]] += sum_dp_i - dp[i][d[s]]
    dp[i + 1][d[s]] %= mod

print(sum(dp[len(S)]) % mod - 1)
