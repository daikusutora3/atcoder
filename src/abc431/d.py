N = int(input())

START = 500 * 500
MAX_W = START * 2 + 1
dp = [-1 for _ in range(MAX_W)]
dp[START] = 0
for i in range(N):
    next_dp = [-1 for _ in range(MAX_W)]
    W, H, B = map(int, input().split())
    for w in range(MAX_W):
        if dp[w] == -1:
            continue
        next_dp[w + W] = max(next_dp[w + W], dp[w] + B) if w + W < MAX_W else None
        next_dp[w - W] = max(next_dp[w - W], dp[w] + H) if w - W >= 0 else None
    dp = next_dp
ans = max(dp[w] for w in range(START, MAX_W))

print(ans)
