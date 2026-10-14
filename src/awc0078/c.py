from atcoder.fenwicktree import FenwickTree

N = int(input())
L = list(map(int, input().split()))
fenwick_tree = FenwickTree(2 * N + 100)

ans = [-1 for i in range(N)]
for i in range(N):
    fenwick_tree.add(L[i], 1)
    ans[L[i] - 1] = i + 1 - fenwick_tree.sum(0, L[i])

print(*ans, sep="\n")
