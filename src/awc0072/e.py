from atcoder.segtree import SegTree

N, M = map(int, input().split())
S = list(map(int, input().split()))
P = list(map(int, input().split()))


segtree = SegTree(min, float("inf"), [S[i] - P[i] for i in range(N)])

for i in range(M):
    L, R = map(int, input().split())
    if segtree.prod(L - 1, R) >= 0:
        print("Yes")
    else:
        print("No")
