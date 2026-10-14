from atcoder.fenwicktree import FenwickTree

N, K = map(int, input().split())
ans = -K
P = list(map(int, input().split()))
fenwick = FenwickTree(N)

for p in P:
    ans += fenwick.sum(p - 1, N)
    fenwick.add(p - 1, 1)


print(max(0, ans))
