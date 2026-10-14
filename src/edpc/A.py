N = int(input())
h = list(map(int, input().split()))

dp = [float("inf") for i in range(N)]
dp[0] = 0

for i in range(1, N):
    for j in range(1, 3):
        if i - j >= 0:
            dp[i] = min(dp[i], abs(h[i] - h[i - j]) + dp[i - j])

print(dp[N - 1])
