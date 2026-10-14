N = int(input())
p = list(map(float, input().split()))

dp = [0 for i in range(N // 2 + 2)]
dp[0] = 1

for i in range(N):
    for j in range(N // 2 + 1, -1, -1):
        if j < N // 2 + 1:
            dp[j] *= 1 - p[i]
        if j - 1 >= 0:
            dp[j] += dp[j - 1] * p[i]
print(dp[N // 2 + 1])
