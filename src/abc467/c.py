N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[float("inf") for j in range(2)] for i in range(N)]

if A[0] == 0:
    dp[0][0] = 0
    dp[0][1] = 1
else:
    dp[0][1] = 0
    dp[0][0] = 1

for i in range(N - 1):
    if B[i] == 0:
        # 偶数 + 偶数
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + (1 if A[i + 1] == 1 else 0))
        # 奇数 + 奇数
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + (1 if A[i + 1] == 0 else 0))
    else:
        # 奇数 + 偶数
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][1] + (1 if A[i + 1] == 1 else 0))
        # 偶数 + 奇数
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][0] + (1 if A[i + 1] == 0 else 0))


print(min(dp[-1]))
