H, W, K = map(int, input().split())
grid = [input() for _ in range(H)]

ans = 0
for top in range(H):
    for bottom in range(top + 1, H + 1):
        for left in range(W):
            for right in range(left + 1, W + 1):
                ones = 0
                for i in range(top, bottom):
                    for j in range(left, right):
                        if grid[i][j] == "1":
                            ones += 1
                if ones == K:
                    ans += 1

print(ans)
