import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())
grid = [input() for i in range(H)]

INF = float("inf")


def to_id(r, c, d):
    return d + (r + c * H) * 4


for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            rs, cs = i, j
        elif grid[i][j] == "G":
            rt, ct = i, j

queue = deque([(rs, cs, d) for d in range(4)])
cost = [INF for i in range(H * W * 4)]
memo = [-1 for i in range(H * W * 4)]
for d in range(4):
    cost[to_id(rs, cs, d)] = 0


direction = [(1, 0, 0), (-1, 0, 1), (0, 1, 2), (0, -1, 3)]
while queue:
    r, c, d = queue.popleft()
    for dr, dc, dd in direction:
        nr, nc = r + dr, c + dc
        if grid[r][c] == "o" and d != dd:
            continue
        if grid[r][c] == "x" and d == dd:
            continue

        if 0 <= nr < H and 0 <= nc < W:
            if grid[nr][nc] != "#":
                if cost[to_id(nr, nc, dd)] == INF:
                    cost[to_id(nr, nc, dd)] = cost[to_id(r, c, d)] + 1
                    memo[to_id(nr, nc, dd)] = d
                    queue.append((nr, nc, dd))

data = {0: "D", 1: "U", 2: "R", 3: "L", -1: "?"}
tmp = INF
d = -1

for i in range(4):
    if cost[to_id(rt, ct, i)] < tmp:
        tmp = cost[to_id(rt, ct, i)]
        d = i


if tmp == INF:
    print("No")
else:
    ans = deque()
    r, c = rt, ct
    for _ in range(tmp):
        ans.appendleft(data[d])
        dr, dc, _ = direction[d]
        d = memo[to_id(r, c, d)]
        r, c = r - dr, c - dc
    print("Yes")
    print("".join(ans))
