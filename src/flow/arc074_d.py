from atcoder.maxflow import MFGraph

H, W = map(int, input().split())
grid = [input() for i in range(H)]

# 0 ~ 2*H*W-1: gridの各マスに対応する頂点
# 2*H*W ~ H*W+H-1: スーパー行頂点
# 2*H*W+H ~ H*W+H+W-1: スーパー列頂点
graph = MFGraph(2 * H * W + H + W)

s = -1
t = -1


def id(i, j):
    global H
    a = j + i * W
    # (入口, 出口)
    return (2 * a, 2 * a + 1)


def row_id(i):
    global H, W
    return 2 * H * W + i


def column_id(j):
    global H, W
    return 2 * H * W + H + j


for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            s = (i, j)
        if grid[i][j] == "T":
            t = (i, j)

        if grid[i][j] != ".":
            # 入り口 -> 出口
            ent, exi = id(i, j)
            if grid[i][j] == "S" or grid[i][j] == "T":
                graph.add_edge(ent, exi, float("inf"))
            else:
                graph.add_edge(ent, exi, 1)
            # スーパー行頂点
            graph.add_edge(exi, row_id(i), float("inf"))
            graph.add_edge(row_id(i), ent, float("inf"))
            # スーパー列頂点
            graph.add_edge(exi, column_id(j), float("inf"))
            graph.add_edge(column_id(j), ent, float("inf"))

ans = graph.flow(id(s[0], s[1])[0], id(t[0], t[1])[1])
print(-1 if ans == float("inf") else ans)
