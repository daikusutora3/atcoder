N = int(input())
XY = [list(map(int, input().split())) for i in range(N)]
X = [XY[i][0] for i in range(N)]
Y = [XY[i][1] for i in range(N)]
ans = float("inf")

X.sort()
Y.sort()

Xr = [0 for i in range(N + 1)]
for i in range(N):
    Xr[i + 1] = X[i] + Xr[i]
Yr = [0 for i in range(N + 1)]
for i in range(N):
    Yr[i + 1] = Y[i] + Yr[i]

for i in range(N):
    res = 0
    res += (Xr[N] - Xr[i]) - (Xr[i]) + (2 * i - N) * X[i]
    res += (Yr[N] - Yr[i]) - (Yr[i]) + (2 * i - N) * Y[i]
    ans = min(ans, res)

print(ans)
