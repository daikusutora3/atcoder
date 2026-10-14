import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline  # これないとTLEしちゃう
N, Q = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(Q)]
A.sort()
answer = []
for _ in range(Q):
    X, Y = XY[_]
    L = bisect_left(A, X)
    lo = X
    hi = X + Y + N
    while lo < hi:
        mid = (lo + hi) // 2
        cnt_forbidden = bisect_right(A, mid) - L
        usable = (mid - X + 1) - cnt_forbidden
        if usable >= Y:
            hi = mid
        else:
            lo = mid + 1
    answer.append(lo)

print(*answer, sep="\n")
