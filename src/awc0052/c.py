N, S = map(int, input().split())

dp = [[-float("inf") for j in range(S + 1)] for i in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    v, c = map(int, input().split())
    for j in range(S + 1):
        # 商品を選ばないとき
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        # 商品を選ぶとき
        if j - c >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - c] + v)

print(-1 if dp[N][S] == -float("inf") else dp[N][S])
