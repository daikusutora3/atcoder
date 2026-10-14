from collections import deque


H, W = map(int, input().split())

g = [input() for i in range(H)]
ag = [[-1] * W for i in range(H)]
q = deque([])

for i in range(H):
    for j in range(W):
        flag = False
        for di, dj in [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if g[ni][nj] == ".":
                flag = True
        if g[i][j] == "#" and flag:
            q.append((i, j))
            ag[i][j] = 0

while q:
    i, j = q.popleft()
    for di, dj in [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if ag[ni][nj] != -1:
            continue
        ag[ni][nj] = (ag[i][j] + 1) % 2
        q.append((ni, nj))

for i in range(H):
    res = []
    for j in range(W):
        if ag[i][j] == 0:
            res.append("#")
        else:
            res.append(".")
    print(*res, sep="")
