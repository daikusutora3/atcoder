from atcoder.maxflow import MFGraph

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = float("inf")
for m in range(1, M + 1):
    # 0 ~ N*(m+1)-1: 各日にちに対応する頂点の番号
    # N*(m+1) ~ N*(m+1)+N*m-1: 分配器頂点
    # N*(2*m+1): 始点
    # N*(2*m+1)+1: 終点
    graph = MFGraph(N * (2 * m + 1) + 2)
    # 始点 -> 0日目の家頂点に対して辺を張る
    for i in range(N):
        graph.add_edge(N * (2 * m + 1), i, A[i])
    # j日目~j+1日目に対して辺を張る
    for j in range(m + 1):
        for i in range(N):
            if j < m and (j == 0 or (j > 0 and B[j - 1] != i + 1)):
                # 自分の家に小豆を残す辺 OK
                graph.add_edge(i + j * N, i + (j + 1) * N, INF)
                # print(f"家: {i + j * N}")
                # 自分の家から分配器への辺 OK
                graph.add_edge(i + j * N, (i + j * N) + (N * (m + 1)), K)
                # 分配器から次のj+1日目の左隣の家と右隣の家への辺 OK
                graph.add_edge(
                    (i + j * N) + (N * (m + 1)), (i - 1) % N + (j + 1) * N, INF
                )
                graph.add_edge(
                    (i + j * N) + (N * (m + 1)), (i + 1) % N + (j + 1) * N, INF
                )

    # 最後の日の家から終点に向かって辺を引く
    for i in range(N):
        if B[m - 1] != i + 1:
            graph.add_edge(i + j * N, N * (2 * m + 1) + 1, INF)

    print(graph.flow(N * (2 * m + 1), N * (2 * m + 1) + 1))
