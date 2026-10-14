H, W = map(int, input().split())
grid = [input() for i in range(H)]

ans = 0

for h1 in range(H):
    for w1 in range(W):
        for h2 in range(h1, H):
            for w2 in range(w1, W):
                flag = True
                for i in range(h1, h2 + 1):
                    for j in range(w1, w2 + 1):
                        if grid[i][j] != grid[h1 + h2 - i][w1 + w2 - j]:
                            flag = False
                if flag:
                    ans += 1

print(ans)
