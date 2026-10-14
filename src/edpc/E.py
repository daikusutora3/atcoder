N, W = map(int, input().split())
wv = [list(map(int, input().split())) for i in range(N)]

dp = [float("inf") for v in range(10**5 + 1)]
dp[0] = 0

for i in range(N):
    for v in range(10**5, -1, -1):
        if v - wv[i][1] >= 0:
            dp[v] = min(dp[v], dp[v - wv[i][1]] + wv[i][0])

ans = 0
for v in range(10**5 + 1):
    if dp[v] <= W:
        ans = v

print(ans)
