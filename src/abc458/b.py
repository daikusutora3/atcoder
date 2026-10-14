H, W = map(int, input().split())

for i in range(H):
    ans = []
    for j in range(W):
        cnt = 0
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W:
                cnt += 1
        ans.append(cnt)
    print(*ans)
