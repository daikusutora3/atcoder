K, M = map(int, input().split())
MOD = 10007 * M
cl = [list(map(int, input().split())) for _ in range(K)]
cl.reverse()

BASE = 30
dp = [[0 for _ in range(10)] for _ in range(BASE + 1)]
pow10 = [0] * (BASE + 1)

for i in range(10):
    dp[0][i] = i % MOD

pow10[0] = 10 % MOD
for k in range(BASE):
    pow10[k + 1] = pow10[k] * pow10[k] % MOD

for k in range(BASE):
    for i in range(10):
        dp[k + 1][i] = (dp[k][i] + dp[k][i] * pow10[k]) % MOD

ans = 0
cur = 1
for i in range(K):
    c, l = cl[i]
    for k in range(BASE):
        if (l >> k) & 1:
            ans = (ans + dp[k][c] * cur) % MOD
            cur = (cur * pow10[k]) % MOD

print((ans // M) % 10007)
