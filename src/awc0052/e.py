from itertools import permutations


N, M, F = map(int, input().split())
R = list(map(int, input().split()))
graph = [[float("inf") for j in range(N)] for i in range(N)]
for i in range(N):
    graph[i][i] = 0

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u - 1][v - 1] = w
    graph[v - 1][u - 1] = w


INF = float("inf")  # 無限大を表す値


def warshall_floyd(graph):
    """
    ワーシャル・フロイド法で全点対間最短経路を計算する

    Args:
        graph: 隣接行列形式のグラフ (2次元リスト)
               graph[i][j] は頂点iからjへの辺のコスト。
               辺が存在しない場合は INF。

    Returns:
        全点対間最短経路の距離行列 (2次元リスト)
    """
    n = len(graph)
    dist = [row[:] for row in graph]  # graph のコピーを作成

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


d = warshall_floyd(graph)

ans = -float("inf")
for kaijou in permutations([i for i in range(1, N)]):
    v = 0
    now = F + R[0]
    check = True
    for u in kaijou:
        now -= d[v][u]
        if now < 0:
            check = False
            break
        now += R[u]
        if u == N - 1:
            ans = max(ans, now)
        v = u
    now -= d[v][N - 1]
    if check:
        ans = max(ans, now)

print(-1 if ans == -float("inf") else ans)
