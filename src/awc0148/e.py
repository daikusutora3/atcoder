N, M, K = list(map(int, input().split()))
t = list(map(int, input().split()))
C = [list(map(int, input().split())) for i in range(N + 1)]

INF = 10**12


def to_id(i, bit):
    return i * (2**M) + bit


dp = [INF for id in range((N + 1) * (2**M))]
ndp = [INF for id in range((N + 1) * (2**M))]
dp[0] = 0
ans = INF

if K == 0:
    for i in range(N + 1):
        ans = min(ans, dp[to_id(i, 0)] + C[i][N - i])
for k in range(N):
    for i in range(k, min(N, N - (K - (k + 1)))):
        for bit in range(2**M):
            for j in range(i + 1):
                # j -> iに移動するよ
                ndp[to_id(i + 1, bit)] = min(
                    ndp[to_id(i + 1, bit)],
                    dp[to_id(j, bit ^ (1 << (t[i] - 1)))] + C[j][i - j],
                )
    dp = ndp
    if k + 1 >= K:
        for i in range(N + 1):
            ans = min(ans, dp[to_id(i, 0)] + C[i][N - i])
    ndp = [INF for id in range((N + 1) * (2**M))]

print(-1 if ans == INF else ans)
