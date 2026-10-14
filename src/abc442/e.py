import bisect
from math import atan2, degrees

N, Q = map(int, input().split())

XY = [list(map(int, input().split())) for _ in range(N)]

degree_data = []

for i in range(N):
    x, y = XY[i]
    degree_data.append(degrees(atan2(x, y)))

degree_data.sort()

for i in range(N):
    degree_data.append(degree_data[i] + 360)

# AとBのそれぞれに対する角度を2分探索

ans = []
for _ in range(Q):
    A, B = map(int, input().split())
    A_deg = degrees(atan2(XY[A - 1][0], XY[A - 1][1]))
    B_deg = degrees(atan2(XY[B - 1][0], XY[B - 1][1]))
    if B_deg < A_deg:
        B_deg += 360
    ans.append(
        bisect.bisect_right(degree_data, B_deg) - bisect.bisect_left(degree_data, A_deg)
    )

print(*ans, sep="\n")
