from collections import defaultdict


N = int(input())
SIZE = 1000
grid = [[0 for j in range(SIZE + 1)] for i in range(SIZE + 1)]

for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    grid[lx][ly] += 1
    grid[lx][ry] -= 1
    grid[rx][ly] -= 1
    grid[rx][ry] += 1

for i in range(SIZE):
    for j in range(SIZE + 1):
        grid[i + 1][j] += grid[i][j]

for j in range(SIZE):
    for i in range(SIZE + 1):
        grid[i][j + 1] += grid[i][j]

ans = defaultdict(int)
for i in range(SIZE + 1):
    for j in range(SIZE + 1):
        ans[grid[i][j]] += 1


for i in range(N):
    print(ans[i + 1])
