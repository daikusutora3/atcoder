from atcoder.fenwicktree import FenwickTree

N, M = map(int, input().split())
fenwick_tree = FenwickTree(N)

S = list(map(int, input().split()))
for i in range(M):
    print(S[i] - fenwick_tree.sum(0, S[i]))
    fenwick_tree.add(S[i] - 1, 1)
