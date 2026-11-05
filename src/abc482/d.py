import sys

N = int(input())
X = list(map(int, input().split()))

INF = float("inf")
if N == 1:
    print(0)
    sys.exit()

for k in range(N):
    res = INF
    if 0 <= k - 1:
        resl = 0
        resl = max(resl, (X[k] - X[0]) // 2)
        resl = max(resl, (X[-1] - X[k - 1]) // 2)
        res = min(res, resl)
    if k + 1 < N:
        resr = 0
        resr = max(resr, (X[k + 1] - X[0]) // 2)
        resr = max(resr, (X[-1] - X[k]) // 2)
        res = min(res, resr)
    print(res)
