from atcoder.maxflow import MFGraph

H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

N = H * W
graph = MFGraph(N + 2)

ans = 0
for i in range(H):
    for j in range(W):
        graph.add_edge(N, i * W + j, A[i][j])
        graph.add_edge(i * W + j, N + 1, 2 * C)
        # 左下にマスがあるなら
        if i + 1 < H and j - 1 >= 0:
            graph.add_edge(N, i * W + j, C)
            graph.add_edge(i * W + j, (i + 1) * W + j - 1, C)
            ans += C
        # 右下にマスがあるなら
        if i + 1 < H and j + 1 < W:
            graph.add_edge(N, i * W + j, C)
            graph.add_edge(i * W + j, (i + 1) * W + j + 1, C)
            ans += C
        ans += A[i][j]


print(-(graph.flow(N, N + 1) - ans))
