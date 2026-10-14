N, M = map(int, input().split())


dist = [[float("inf") for j in range(N)] for i in range(N)]
for i in range(M):
    u, v, w = map(int, input().split())
    dist[u - 1][v - 1] = w
    dist[v - 1][u - 1] = w

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


dp = [[float("inf") for __ in range(N)] for _ in range(2**N)]

for v in range(1, N):
    dp[1 << v][v] = dist[0][v]

for bit in range(0, 2**N):
    for u in range(N):
        for v in range(N):
            # u番目のbitが立っていますか？(もう行ったことがあるから)
            if bit >> u & 1:
                # bitの中でv番目を1にする
                dp[bit | 1 << v][v] = min(dp[bit | 1 << v][v], dp[bit][u] + dist[u][v])

ans = dp[2**N - 1][0]
print(ans if ans != float("inf") else -1)
