from collections import deque


N, M = map(int, input().split())
grid = [input() for i in range(N)]

# (i, j)
cost = [[float("inf") for j in range(M)] for i in range(N)]
queue = deque([(0, 0)])
cost[0][0] = 0
while queue:
    i, j = queue.popleft()
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni = i + di
        nj = j + dj
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            continue
        n_cost = cost[i][j] + (1 if grid[ni][nj] == "#" else 0)
        if cost[ni][nj] > n_cost:
            cost[ni][nj] = n_cost
            queue.append((ni, nj))

print(cost[N - 1][M - 1])
