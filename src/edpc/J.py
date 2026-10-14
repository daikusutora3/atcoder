N = int(input())

a = list(map(int, input().split()))


dp = [[[0 for k in range(N + 2)] for j in range(N + 2)] for i in range(N + 2)]

for i in range(N + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            if i == 0 and j == 0 and k == 0:
                continue
            dp[i][j][k] = N
            if i - 1 >= 0:
                dp[i][j][k] += dp[i - 1][j + 1][k] * i
            if j - 1 >= 0:
                dp[i][j][k] += dp[i][j - 1][k + 1] * j
            if k - 1 >= 0:
                dp[i][j][k] += dp[i][j][k - 1] * k
            dp[i][j][k] /= i + j + k


# def dfs(i, j, k):
#     global N
#     if i == 0 and j == 0 and k == 0:
#         dp[0][0][0] = 0
#         return 0
#     res = N
#     if i - 1 >= 0:
#         res += dfs(i - 1, j + 1, k) * i
#     if j - 1 >= 0:
#         res += dfs(i, j - 1, k + 1) * j
#     if k - 1 >= 0:
#         res += dfs(i, j, k - 1) * k
#     return res / (i + j + k)


print(dp[a.count(3)][a.count(2)][a.count(1)])
