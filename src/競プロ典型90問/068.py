from atcoder.segtree import SegTree

N = int(input())
Q = int(input())
a = [-float("inf") for i in range(N)]
segtree = SegTree(lambda x, y: x + y, 0, a)

for _ in range(Q):
    T, X, Y, V = map(int, input().split())
    flag = False
    if Y < X:
        X, Y = Y, X
        flag = True
    if T == 0:
        segtree.set(X - 1, V if X % 2 else -V)
    else:
        ans = [
            segtree.prod(X - 1, Y - 1)
            * (1 if ((Y - 1) % 2 if flag else X % 2) else -1)
            * (-1 if (Y - X + 1) % 2 else 1),
            V if (Y - X + 1) % 2 else -V,
        ]
        # print(f"{X}, {Y - X + 1}: {ans}, {sum(ans)}")
        ans = sum(ans)
        print("Ambiguous" if abs(ans) == float("inf") else ans)
