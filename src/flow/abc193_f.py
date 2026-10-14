from atcoder.maxflow import MFGraph

N = int(input())
grid = [input() for _ in range(N)]

# 0~N*N-1: gridの頂点
# N*N: 始点の頂点
# N*N+1: 終点の頂点
graph = MFGraph(N * N + 2)


def id(i, j):
    return i + j * N


for i in range(N):
    for j in range(N):
        if (i + j) % 2:
            if grid[i][j] == "B":
                graph.add_edge(N * N, id(i, j), 4)
            elif grid[i][j] == "W":
                graph.add_edge(id(i, j), N * N + 1, 4)
        else:
            if grid[i][j] == "W":
                graph.add_edge(N * N, id(i, j), 4)
            elif grid[i][j] == "B":
                graph.add_edge(id(i, j), N * N + 1, 4)
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            graph.add_edge(id(i, j), id(ni, nj), 1)

res = graph.flow(N * N, N * N + 1)
# print(f"{N * (N - 1) * 2} - {res}")
print(N * (N - 1) * 2 - res)
