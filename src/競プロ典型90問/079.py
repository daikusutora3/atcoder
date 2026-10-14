from collections import deque


H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
B = [list(map(int, input().split())) for i in range(H)]

queue = deque([(0, 0)])
visited = {(0, 0)}
ans = 0
while queue:
    i, j = queue.popleft()
    cnt = B[i][j] - A[i][j]
    if 0 <= i < H - 1 and 0 <= j < W - 1:
        A[i][j] += cnt
        A[i + 1][j] += cnt
        A[i][j + 1] += cnt
        A[i + 1][j + 1] += cnt
        ans += abs(cnt)
    else:
        if cnt != 0:
            ans = -1
            break
    for di, dj in [(1, 0), (0, 1)]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if (ni, nj) not in visited:
            visited.add((ni, nj))
            queue.append((ni, nj))

if ans == -1:
    print("No")
else:
    print("Yes")
    print(ans)
