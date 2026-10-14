K = input()
D = int(input())
mod = 10**9 + 7
# dp[i][m][b]:
# i: 先頭からi桁目までを処理している
# m: 今までとった値の総和のmod
# b: 0のときは先頭からi桁目までが一致している、1なら先頭からi桁目よりも小さい
dp = [[[0 for i in range(2)] for m in range(D)] for _ in range(len(K) + 1)]
dp[0][0][0] = 1


for i in range(len(K)):
    for m in range(D):
        for a in range(10):
            if a == int(K[i]):
                dp[i + 1][(m + a) % D][0] += dp[i][m][0]
                dp[i + 1][(m + a) % D][0] %= mod
            if a < int(K[i]):
                dp[i + 1][(m + a) % D][1] += dp[i][m][0]
                dp[i + 1][(m + a) % D][1] %= mod
            dp[i + 1][(m + a) % D][1] += dp[i][m][1]
            dp[i + 1][(m + a) % D][1] %= mod

print((sum(dp[len(K)][0]) - 1) % mod)
