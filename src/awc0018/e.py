N, K, B = map(int, input().split())
CS = [list(map(int, input().split())) for i in range(N)]

dp = [
    [[float("inf") for b in range(B + 1)] for k in range(K + 1)] for i in range(N + 1)
]

dp[0][0][0] = 0

for i in range(N):
    for k in range(K + 1):
        for b in range(B + 1):
            dp[i + 1][k][b] = min(dp[i + 1][k][b], dp[i][k][b])

            if (
                b - CS[i][0] >= 0
                and (dp[i][k - 1][b - CS[i][0]] < CS[i][1])
                and k - 1 >= 0
            ):
                dp[i + 1][k][b] = min(dp[i + 1][k][b], CS[i][1])

ans = 0
for k in range(0, K + 1):
    if min(dp[N][k]) < float("inf"):
        ans = k
print(ans)
