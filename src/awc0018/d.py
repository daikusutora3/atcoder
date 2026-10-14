N, K = map(int, input().split())
C = list(map(int, input().split()))
dp = [[False for k in range(K + 1)] for i in range(N + 1)]
dp[0][0] = True

for i in range(N):
    for k in range(K + 1):
        dp[i + 1][k] |= dp[i][k]
        if k - C[i] >= 0:
            dp[i + 1][k] |= dp[i][k - C[i]]

ans = -1

for k in range(K + 1):
    if dp[N][k]:
        ans = k

print(ans)
