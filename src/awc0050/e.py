N, M = map(int, input().split())
C = list(map(int, input().split()))
E = [list(map(int, input().split())) for i in range(N)]
bit_E = [0 for i in range(N)]
for i in range(N):
    for j in range(M):
        if E[i][j]:
            bit_E[i] |= 1 << j

dp = [float("inf") for i in range(2**M)]
dp[0] = 0
for bit in range(2**M):
    for i in range(N):
        dp[bit | bit_E[i]] = min(dp[bit | bit_E[i]], dp[bit] + C[i])

print(-1 if dp[2**M - 1] == float("inf") else dp[2**M - 1])
