from collections import defaultdict


N, M, K = map(int, input().split())
N, M, K = M, K, N
dist = [[float("inf") for j in range(N)] for i in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    dist[u - 1][v - 1] = w
    dist[v - 1][u - 1] = w

for i in range(N):
    dist[i][i] = 0


for k in range(N):  # 中継点
    for i in range(N):  # 始点
        for j in range(N):  # 終点
            # 繰り返し見ていくので、現時点の i から j へ向かうコスト と 今検証している k を経由して j に向かうコスト の小さい方を i から j へ向かうコストとして登録する
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0
for _ in range(K):
    S, T = map(int, input().split())
    ans += dist[S - 1][T - 1]

print(ans)
