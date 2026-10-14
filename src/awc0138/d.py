import sys

input = sys.stdin.readline

N, W, B = map(int, input().split())

INF = float("inf")
dp = [[-INF for w in range(W + 1)] for f in range(3)]
ndp = [[-INF for w in range(W + 1)] for f in range(3)]
dp[0][0] = 0


for i in range(N):
    D, C = map(int, input().split())
    for w in range(W + 1):
        # i番目を取らなかった時
        ndp[0][w] = max(ndp[0][w], dp[0][w], dp[1][w], dp[2][w])
        # i番目を取った時
        if w - C >= 0:
            ndp[1][w] = max(ndp[1][w], dp[0][w - C] + D)
        if w - C >= 0:
            ndp[2][w] = max(ndp[2][w], dp[1][w - C] + D + 2 * B, dp[2][w - C] + D + B)
    dp = ndp
    ndp = [[-INF for w in range(W + 1)] for f in range(3)]

print(max(max(dp[0]), max(dp[1]), max(dp[2])))
