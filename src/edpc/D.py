N, W = map(int, input().split())
wv = [list(map(int, input().split())) for i in range(N)]

dp = [0 for w in range(W + 1)]
for i in range(N):
    for w in range(W, -1, -1):
        if w - wv[i][0] >= 0:
            dp[w] = max(dp[w], dp[w - wv[i][0]] + wv[i][1])

print(dp[W])
