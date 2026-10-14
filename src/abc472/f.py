from atcoder.maxflow import MFGraph
from atcoder.scc import SCCGraph

H, W = map(int, input().split())
grid = [input() for i in range(H)]
graph = SCCGraph(H * W)
ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == "+":
            ans += 1
        elif grid[i][j] == "-":
            ans -= 1
        if grid[i][j] == "#":
            continue
        for di, dj in [[1, 0], [0, 1], [0, -1]]:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if grid[ni][nj] == "#":
                continue
            graph.add_edge(i + j * H, ni + nj * H)

scc = graph.scc()
group_to_cost = [0 for i in range(len(scc))]

for id, group in enumerate(scc):
    if grid[group[0] % H][group[0] // H] == "#":
        continue
    cost = 0
    for ij in group:
        i, j = ij % H, ij // H
        if grid[i][j] == "+":
            cost += 1
        elif grid[i][j] == "-":
            cost -= 1
    group_to_cost[id] = cost


# len(scc): S
# len(scc)+1: T
graph = MFGraph(len(scc) + 2)
C = 10**10

for id in range(len(scc)):
    graph.add_edge(len(scc), id, C)
    graph.add_edge(id, len(scc) + 1, group_to_cost[id] + C)

# id1の頂点からid2の頂点に対して辺があるかどうかを判定して、あるならば無限の辺をMGGraphに引く
for id1 in range(len(scc)):
    for id2 in range(len(scc)):
        flag = False
        if id1 == id2:
            continue
        for v in scc[id1]:
            for u in scc[id2]:
                vi, vj = v % H, v // H
                ui, uj = u % H, u // H
                if grid[vi][vj] == "#" or grid[ui][uj] == "#":
                    continue
                if vj == uj and vi + 1 == ui:
                    flag = True
        if flag:
            graph.add_edge(id1, id2, float("inf"))


print(ans - (graph.flow(len(scc), len(scc) + 1) - C * len(scc)))
