import sys
from collections import deque

input = sys.stdin.readline

dy = {"up": 0, "down": 0, "right": 1, "left": -1}
dx = {"up": -1, "down": 1, "right": 0, "left": 0}
ty_to_di = {
    "A": {"right": "right", "down": "down", "up": "up", "left": "left"},
    "B": {"right": "down", "down": "right", "up": "left", "left": "up"},
    "C": {"right": "up", "down": "left", "up": "right", "left": "down"},
}
MAX_COST = 10**9


def next_position(x, y, di, ty):
    return (x + dx[ty_to_di[ty][di]], y + dy[ty_to_di[ty][di]])


def solve():
    H, W = map(int, input().split())
    GRID = [input() for _ in range(H)]
    cost = [
        [
            {"up": MAX_COST, "down": MAX_COST, "right": MAX_COST, "left": MAX_COST}
            for _ in range(W + 1)
        ]
        for __ in range(H)
    ]
    # (cost, (x, y), di)
    queue = deque([(0, (0, 0), "right")])
    while queue:
        c, (x, y), di = queue.popleft()
        if cost[x][y][di] <= c:
            continue
        cost[x][y][di] = c
        if y == W:
            continue
        # print(f"c: {c}, (x, y): {x, y}, di: {di}")
        for ty in ["A", "B", "C"]:
            nx, ny = next_position(x, y, di, ty)
            if 0 <= nx and nx < H and 0 <= ny and ny <= W:
                queue.append(
                    (c if GRID[x][y] == ty else c + 1, (nx, ny), ty_to_di[ty][di])
                )
    return cost[H - 1][W]["right"]


T = int(input())
answers = []
for _ in range(T):
    ans = solve()
    answers.append(ans)

print(*answers, sep="\n")
