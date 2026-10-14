from atcoder.maxflow import MFGraph

N, M = map(int, input().split())
grid = [list(input()) for i in range(N)]


# 0~N*M-1: グリッドのマス頂点
# N*M: 始点
# N*M+1: 終点
g = MFGraph(N * M + 2)

for i in range(N):
    for j in range(M):
        if grid[i][j] == "#" or (i + j) % 2 == 0:
            continue
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if grid[ni][nj] == ".":
                g.add_edge(i + j * N, ni + nj * N, 1)

for i in range(N):
    for j in range(M):
        if (i + j) % 2 == 0:
            g.add_edge(i + j * N, N * M + 1, 1)
        else:
            g.add_edge(N * M, i + j * N, 1)

print(g.flow(N * M, N * M + 1))

for e in g.edges():
    if e.flow == 0 or e.src >= N * M or e.dst >= N * M:
        continue
    # print(f"{(e.src % N, e.src // N)} -> {(e.dst % N, e.dst // N)}")
    i, j = e.src % N, e.src // N
    ni, nj = e.dst % N, e.dst // N
    if i == ni:
        if j > nj:
            j, nj = nj, j
        grid[i][j] = ">"
        grid[i][nj] = "<"
    elif j == nj:
        if i > ni:
            i, ni = ni, i
        grid[i][j] = "v"
        grid[ni][j] = "^"

for a in grid:
    print("".join(a))
