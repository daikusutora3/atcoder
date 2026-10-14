N = int(input())
C = [list(map(int, input().split())) for i in range(N - 1)]

ans = False
for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            if C[a][c - a - 1] > C[a][b - a - 1] + C[b][c - b - 1]:
                ans = True

print("Yes" if ans else "No")
