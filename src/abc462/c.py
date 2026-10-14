N = int(input())
XY = [list(map(int, input().split())) for i in range(N)]

ans = 0
minY = float("inf")

XY.sort()

for i in range(N):
    x, y = XY[i]
    if y <= minY:
        minY = y
        ans += 1

print(ans)
