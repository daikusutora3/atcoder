# N, K = map(int, input().split())
# h = list(map(int, input().split()))

# dp = [float("inf") for i in range(N)]
# dp[0] = 0

# for i in range(1, N):
#     for j in range(1, K + 1):
#         if i - j >= 0:
#             dp[i] = min(dp[i], abs(h[i] - h[i - j]) + dp[i - j])

# print(dp[N - 1])

from cmath import log


print(log(10**5, 2))
