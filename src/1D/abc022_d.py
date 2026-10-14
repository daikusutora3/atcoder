from math import sqrt

N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(N)]


def centroid(xys):
    rx = 0
    ry = 0
    if len(xys) == 0:
        return (0, 0)

    for x, y in xys:
        rx += x
        ry += y
    return (rx / len(xys), ry / len(xys))


ca = centroid(A)
min_a_dist = float("inf")
cb = centroid(B)
min_b_dist = float("inf")


for x, y in A:
    dist = sqrt((ca[0] - x) ** 2 + (ca[1] - y) ** 2)
    if dist == 0:
        continue
    min_a_dist = min(min_a_dist, dist)

for x, y in B:
    dist = sqrt((cb[0] - x) ** 2 + (cb[1] - y) ** 2)
    if dist == 0:
        continue
    min_b_dist = min(min_b_dist, dist)

print(min_b_dist / min_a_dist)
