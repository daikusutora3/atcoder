H, W = map(int, input().split())

grid = [input() for i in range(H)]

flag = True
t, b, l, r = float("inf"), -float("inf"), float("inf"), -float("inf")
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            flag = False
            t = min(t, i)
            b = max(b, i)
            r = max(r, j)
            l = min(l, j)

if flag:
    print(0)
else:
    print(2 * (b - t + r - l + 2))
