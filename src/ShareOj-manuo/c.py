N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]
INF = float("inf")
dp = [[-INF for bit in range(2**N)] for i in range(M + 1)]
dp[0][0] = 0

for i in range(M):
    for bit in range(2**N):
        shunyu = 1
        for j in range(N):
            if bit >> j & 1:
                shunyu += AB[j][1]
        for j in range(N):
            if not bit >> j & 1 and dp[i][bit] + shunyu - AB[j][0] >= 0:
                dp[i + 1][bit | 1 << j] = max(
                    dp[i + 1][bit | 1 << j], dp[i][bit] + shunyu - AB[j][0]
                )
        dp[i + 1][bit] = max(dp[i + 1][bit], dp[i][bit] + shunyu)

ans = float("inf")
for i in range(M + 1):
    for bit in range(2**N):
        if dp[i][bit] >= M:
            ans = min(ans, i)

print(ans)
