N, D = map(int, input().split())
CF = [list(map(int, input().split())) for i in range(N)]


dp = [[float("inf") for j in range(D + 1)] for i in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    C, F = CF[i]
    for j in range(D + 1):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        dp[i + 1][j] = min(dp[i + 1][j], dp[i + 1][max(0, j - F)] + C)


print(dp[N][D])
