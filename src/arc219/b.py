from atcoder.fenwicktree import FenwickTree

mod = 998244353

T = int(input())


def solve():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    if P == sorted(P):
        ans += 1
    fenwick_tree = FenwickTree(N)
    flag = True
    for i in range(N):
        fenwick_tree.add(P[i] - 1, 1)
        if flag and P[i] - 1 == i:
            # print(
            #     f"P[{i}]: {P[i]}, P[i]より大きい数字の数: {N - fenwick_tree.sum(0, P[i])}"
            # )
            ans += N - fenwick_tree.sum(0, P[i])
            ans %= mod
        else:
            flag = False
    return ans


for _ in range(T):
    print(solve())
