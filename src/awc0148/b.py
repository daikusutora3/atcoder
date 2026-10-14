from collections import defaultdict

N = int(input())

cntX = defaultdict(int)
cntY = defaultdict(int)

XY = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    X, Y = XY[i]
    cntX[X] += 1
    cntY[Y] += 1

Cx = len(cntX.keys())
Cy = len(cntY.keys())


for i in range(N):
    X, Y = XY[i]
    print(
        (Cx - (1 if cntX[X] == 1 else 0)) * (Cy - (1 if cntY[Y] == 1 else 0)) - (N - 1)
    )
