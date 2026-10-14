import sys

from atcoder.segtree import SegTree

input = sys.stdin.readline  # 速くするだけ、書き味はそのまま

N, Q = map(int, input().split())
A = list(map(int, input().split()))

VMAX = 500000
SIZE = VMAX + 1  # 値は 0..500000。prod(0, r+1) を使うので +1 で十分

# 値ごとの個数と総和を用意（位置ではなく値の分布）
cnt_init = [0] * SIZE
sum_init = [0] * SIZE
for a in A:
    cnt_init[a] += 1
    sum_init[a] += a

# 区間和用の SegTree を 2 本（個数・総和）用意
op = lambda x, y: x + y
e = 0
seg_cnt = SegTree(op, e, cnt_init)  # 値ごとの個数を区間和
seg_sum = SegTree(op, e, sum_init)  # 値ごとの総和を区間和

ans = []
for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, x, y = map(int, query.split())
        x -= 1
        old = A[x]
        if old != y:
            # old を 1 個減らし、y を 1 個増やす（値側の2点更新）
            seg_cnt.set(old, seg_cnt.get(old) - 1)
            seg_sum.set(old, seg_sum.get(old) - old)
            seg_cnt.set(y, seg_cnt.get(y) + 1)
            seg_sum.set(y, seg_sum.get(y) + y)
            A[x] = y
    else:
        _, l, r = map(int, query.split())
        if l > r:
            ans.append(l * N)  # clamp は全部 l になる
        else:
            # #(A<l), Σ_{A<l}A
            cnt_lt = seg_cnt.prod(0, l)
            sum_lt = seg_sum.prod(0, l)
            # #(A≤r), Σ_{A≤r}A
            cnt_le = seg_cnt.prod(0, r + 1)
            sum_le = seg_sum.prod(0, r + 1)
            # clamp の総和 = l*#(A<l) + Σ_{l≤A≤r}A + r*#(A>r)
            total = l * cnt_lt + (sum_le - sum_lt) + r * (N - cnt_le)
            ans.append(total)

print(*ans, sep="\n")
