from collections import deque


H, W = map(int, input().split())
grid = [input() for i in range(H)]

ans = -1
for si in range(H):
    for sj in range(W):
        if grid[si][sj] == "#":
            continue
        queue = deque([[(si, sj)]])
        while queue:
            p = queue.popleft()
            i, j = p[-1]
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if not (0 <= ni < H and 0 <= nj < W):
                    continue
                if grid[ni][nj] == "#":
                    continue
                if (ni, nj) == (si, sj) and len(p) >= 3:
                    ans = max(ans, len(p))
                    continue
                if (ni, nj) in p:
                    continue
                queue.append(p + [(ni, nj)])


print(ans)
