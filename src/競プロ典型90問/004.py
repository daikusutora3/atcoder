H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

r_g = [[0 for j in range(W + 1)] for i in range(H + 1)]
r_r = [[0 for j in range(W + 1)] for i in range(H + 1)]

for i in range(H):
    for j in range(W):
        r_g[i][j + 1] += r_g[i][j] + A[i][j]

for j in range(W):
    for i in range(H):
        r_r[i + 1][j] += r_r[i][j] + A[i][j]

B = [[0 for j in range(W)] for i in range(H)]

for i in range(H):
    for j in range(W):
        B[i][j] = r_g[i][W] + r_r[H][j] - A[i][j]

for b in B:
    print(*b)
