N = int(input())
a = list(map(int, input().split()))
dp = [[float("inf") for r in range(N + 1)] for l in range(N)]

for i in range(N):
    dp[i][i + 1] = 0

ruia = [0 for i in range(N + 1)]
for i in range(N):
    ruia[i + 1] += ruia[i] + a[i]
for l in range(N - 1, -1, -1):
    for r in range(l + 1, N + 1):
        # print(f"=={l}~{r}==")
        for i in range(l, r):
            dp[l][r] = min(
                dp[l][r],
                (ruia[i] - ruia[l]) + (ruia[r] - ruia[i]) + dp[l][i] + dp[i][r],
            )
        # print(dp[l][r])

print(dp[0][N])
