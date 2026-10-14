H, W = map(int, input().split())
grid = [input() for i in range(H)]

row_data = [[0 for _ in range(26)] for i in range(H)]
column_data = [[0 for _ in range(26)] for j in range(W)]

for i in range(H):
    for j in range(W):
        row_data[i][ord(grid[i][j]) - ord("a")] += 1

for j in range(W):
    for i in range(H):
        column_data[j][ord(grid[i][j]) - ord("a")] += 1


ans = []
for i in range(H):
    for j in range(W):
        if (
            row_data[i][ord(grid[i][j]) - ord("a")] == 1
            and column_data[j][ord(grid[i][j]) - ord("a")] == 1
        ):
            ans.append(grid[i][j])

print("".join(ans))
