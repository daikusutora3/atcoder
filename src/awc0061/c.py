N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [-float("inf") for i in range(N + 1)]
dp[0] = 0

for i in range(1, N + 1):
    # i番目の果物をとるとき
    if i - K - 1 >= 0:
        dp[i] = max(dp[i], dp[i - K - 1] + A[i - 1])
    # i-Kが0未満のとき
    else:
        dp[i] = max(dp[i], dp[0] + A[i - 1])
    # i番目の果物をとらないとき
    dp[i] = max(dp[i], dp[i - 1])

print(dp[N])
