from sortedcontainers import SortedList


W, N = map(int, input().split())
dp = [[-float("inf") for w in range(W + 1)] for i in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    L, R, V = map(int, input().split())
    sl = SortedList()
    for w in range(W + 1):
        if w - L >= 0:
            sl.add(dp[i][w - L])
        if w - R - 1 >= 0 and len(sl) > R - L:
            sl.remove(dp[i][w - R - 1])
        dp[i + 1][w] = dp[i][w]
        if len(sl):
            dp[i + 1][w] = max(dp[i + 1][w], sl[-1] + V)

print(-1 if dp[N][W] == -float("inf") else dp[N][W])
