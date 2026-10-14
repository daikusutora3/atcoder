N, K = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]

dp = [[-float("inf") for k in range(K + 1)] for _ in range(2)]
ndp = [[-float("inf") for k in range(K + 1)] for _ in range(2)]
dp[0][0] = 0

for i in range(N):
    for k in range(K + 1):
        # o -> o
        ndp[0][k] = max(ndp[0][k], dp[0][k] + AB[i][0])
        # u -> o
        ndp[0][k] = max(ndp[0][k], dp[1][k] + AB[i][0])
        # u -> u
        ndp[1][k] = max(ndp[1][k], dp[1][k] + AB[i][1])
        # o -> u
        if k - 1 >= 0:
            ndp[1][k] = max(ndp[1][k], dp[0][k - 1] + AB[i][1])
    dp = ndp
    ndp = [[-float("inf") for k in range(K + 1)] for _ in range(2)]

print(max(max(dp[0]), max(dp[1])))
