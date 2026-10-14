from collections import deque

H, W, K = map(int, input().split())

grid = [input() for i in range(H)]

ban_i = set()
ban_j = set()

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            ban_i.add(i)
            ban_j.add(j)


cost = [[-1 for j in range(W)] for i in range(H)]
queue = deque()

for i in range(H):
    for j in range(W):
        if (i not in ban_i) and (j not in ban_j):
            queue.append((i, j))
            cost[i][j] = 0


while len(queue):
    i, j = queue.popleft()
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if cost[ni][nj] != -1:
            continue
        if grid[ni][nj] == "#":
            continue
        cost[ni][nj] = cost[i][j] + 1
        queue.append((ni, nj))


ans = 0
for i in range(H):
    for j in range(W):
        if cost[i][j] != -1 and cost[i][j] <= K:
            ans += 1

print(ans)
