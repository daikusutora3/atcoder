N, K = map(int, input().split())
XY = [list(map(int, input().split())) for i in range(N)]

dp = [[float("inf") for j in range(K + 1)] for i in range(2**N)]
dp[0][0] = 0

set_to_cost = [0 for i in range(2**N)]

for S in range(2**N):
    res = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (S >> i & 1) and (S >> j & 1):
                res = max(
                    res, abs(XY[i][0] - XY[j][0]) ** 2 + abs(XY[i][1] - XY[j][1]) ** 2
                )
    set_to_cost[S] = res

for S in range(2**N):
    dp[S][1] = min(dp[S][1], set_to_cost[S])
    for k in range(K):
        T = S
        while T:
            S_minus_T = S ^ T
            S_minus_T_cost = set_to_cost[S_minus_T]
            dp[S][k + 1] = min(dp[S][k + 1], max(dp[T][k], S_minus_T_cost))
            T = (T - 1) & S

print(dp[2**N - 1][K])
