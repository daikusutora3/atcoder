from atcoder.segtree import SegTree

N, Q = map(int, input().split())
D = []
for i in range(N):
    a, b, c = map(int, input().split())
    D.append(a - b - c)

P = [0 for i in range(2 * N + 1)]
for i in range(2 * N):
    P[i + 1]

T = sum(D)
segtree = SegTree(min, float("inf"), P)

for _ in range(Q):
    L, S = map(int, input().split())
    L -= 1
    if T >= 0:
        mr = segtree.max_right(L, lambda v: v - P[L] < S)
        print(mr)
    else:
        # これが最悪の増減
        S -= P[L + N] - P[L]
