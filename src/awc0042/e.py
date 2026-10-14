from atcoder.segtree import SegTree

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0 for i in range(N + 1)]
for i in range(N):
    S[i + 1] = S[i] + A[i]
seg1 = SegTree(max, -float("inf"), N + 1)
seg2 = SegTree(max, -float("inf"), N + 1)
seg1.set(0, 0)
seg2.set(0, 0)

for i in range(1, N + 1):
    # 2 -> 1の遷移
    seg1.set(i, seg2.prod(max(0, i - K + 1), i) + S[i])
    # 1 -> 2の遷移
    seg2.set(i, seg1.prod(max(0, i - M + 1), i) - S[i])

print(seg1.prod(N - M + 1, N + 1))
