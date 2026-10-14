from collections import deque


H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
grid = [input() for i in range(H)]

queue = deque([(rs - 1, cs - 1, d) for d in range(4)])
cost = [[[float("inf") for d in range(4)] for j in range(W)] for i in range(H)]
for d in range(4):
    cost[rs - 1][cs - 1][d] = 0


while queue:
    r, c, d = queue.popleft()
    for dr, dc, dd in [(1, 0, 0), (-1, 0, 1), (0, 1, 2), (0, -1, 3)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == ".":
            new_cost = 0 if dd == d else 1
            if cost[nr][nc][dd] > cost[r][c][d] + new_cost:
                cost[nr][nc][dd] = cost[r][c][d] + new_cost
                queue.append((nr, nc, dd)) if new_cost == 1 else queue.appendleft(
                    (nr, nc, dd)
                )

print(min(cost[rt - 1][ct - 1]))
