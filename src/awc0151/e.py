N, K = map(int, input().split())

RD = [list(map(int, input().split())) for i in range(N)]

INF = float("inf")
dp = [[-INF, -INF] for k in range(K + 1)]
ndp = [[-INF, -INF] for k in range(K + 1)]

dp[0][0] = 0


for i in range(N):
    for k in range(K):
        ndp[k + 1][1] = max(ndp[k + 1][1], dp[k][0] + RD[i][0])
        if i - 1 >= 0:
            ndp[k + 1][1] = max(
                ndp[k + 1][1], dp[k][1] + RD[i][0] - min(RD[i][1], RD[i - 1][1])
            )
    for k in range(K + 1):
        ndp[k][0] = max(ndp[k][0], dp[k][1], dp[k][0])
    dp = ndp
    ndp = [[-INF, -INF] for k in range(K + 1)]


print(max(dp[K]))
