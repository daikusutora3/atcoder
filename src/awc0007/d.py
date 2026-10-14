N, A, B = map(int, input().split())

grid_tak = [[0 for __ in range(N + 1)] for _ in range(N + 1)]
grid_aok = [[0 for __ in range(N + 1)] for _ in range(N + 1)]

for _ in range(A):
    r1, c1, r2, c2 = map(int, input().split())
    h = r2 - r1
    w = c2 - c1
    grid_tak[r1 - 1][c1 - 1] += 1
    grid_tak[r1 + h][c1 - 1] += -1
    grid_tak[r1 - 1][c1 + w] += -1
    grid_tak[r1 + h][c1 + w] += 1

for _ in range(B):
    r1, c1, r2, c2 = map(int, input().split())
    h = r2 - r1
    w = c2 - c1
    grid_aok[r1 - 1][c1 - 1] += 1
    grid_aok[r1 + h][c1 - 1] += -1
    grid_aok[r1 - 1][c1 + w] += -1
    grid_aok[r1 + h][c1 + w] += 1


for i in range(0, N + 1):
    for j in range(1, N + 1):
        grid_tak[i][j] += grid_tak[i][j - 1]
        grid_aok[i][j] += grid_aok[i][j - 1]

for j in range(0, N + 1):
    for i in range(1, N + 1):
        grid_tak[i][j] += grid_tak[i - 1][j]
        grid_aok[i][j] += grid_aok[i - 1][j]

ans = 0
for i in range(N):
    for j in range(N):
        if grid_tak[i][j] > 0 and grid_aok[i][j] > 0:
            ans += 1

print(ans)
