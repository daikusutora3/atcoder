from math import atan, cos, degrees, pi, sin, sqrt


T = int(input())
L, X, Y = map(int, input().split())


def solve():
    E = int(input())
    rad = pi / 2 + 2 * pi * (E / T)
    # zahyo = [0, L / 2 * (cos(rad)), L / 2 * (1 - sin(rad))]
    bunbo = sqrt(X**2 + (abs(Y - L / 2 * (cos(rad))) ** 2))
    bunshi = L / 2 * (1 - sin(rad))
    res = degrees(atan(bunshi / bunbo))
    return res


Q = int(input())
for _ in range(Q):
    print(solve())
