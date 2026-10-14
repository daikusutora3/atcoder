N, M = map(int, input().split())

RT = [list(map(int, input().split())) for _ in range(N)]
dp = [-float("inf") for i in range((N + 1) * (M + 1))]

dp[0] = 0


def f(i, j):
    global N
    return i + j * (N + 1)


for i in range(1, N + 1):
    R, T = RT[i - 1]
    for j in range(M + 1):
        # i番目のものをとるとき
        if j - T >= 0:
            dp[f(i, j)] = max(dp[f(i, j)], dp[f(i - 1, j - T)] + R)
        # i番目のものを取らない時
        dp[f(i, j)] = max(dp[f(i, j)], dp[f(i - 1, j)])

print(max(dp))


# N, M = map(int, input().split())

# RT = [list(map(int, input().split())) for _ in range(N)]
# dp = [[-float("inf") for j in range(M + 1)] for i in range(N + 1)]

# dp[0][0] = 0


# for i in range(1, N + 1):
#     R, T = RT[i - 1]
#     for j in range(M + 1):
#         # i番目のものをとるとき
#         if j - T >= 0:
#             dp[i][j] = max(dp[i][j], dp[i - 1][j - T] + R)
#         # i番目のものを取らない時
#         dp[i][j] = max(dp[i][j], dp[i - 1][j])

# print(max(dp[N]))
