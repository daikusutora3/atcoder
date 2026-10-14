H, W = map(int, input().split())
grid = [input() for i in range(H)]
ans = []

for i in range(H):
    for j in range(W):
        if grid[i][j] == "T":
            ans.append((i + 1, j + 1))

print(len(ans))
for a in ans:
    print(*a)
