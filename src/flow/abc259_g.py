from atcoder.maxflow import MFGraph

H, W = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(H)]

# 0~H-1: 行頂点
# H~H+W-1: 列頂点
# H+W: 始点
# H+W+1: 終点
graph = MFGraph(H + W + 2)

ans = 0
for i in range(H):
    ri = sum(grid[i])
    if ri >= 0:
        ans += ri
        graph.add_edge(H + W, i, ri)
    else:
        graph.add_edge(i, H + W + 1, -ri)


for j in range(W):
    cj = 0
    for i in range(H):
        cj += grid[i][j]
    if cj < 0:
        graph.add_edge(H + W, H + j, -cj)
    else:
        ans += cj
        graph.add_edge(H + j, H + W + 1, cj)

for i in range(H):
    for j in range(W):
        if grid[i][j] >= 0:
            graph.add_edge(i, H + j, grid[i][j])
        else:
            graph.add_edge(i, H + j, float("inf"))

print(ans - graph.flow(H + W, H + W + 1))
