N = int(input())

wsv = [list(map(int, input().split())) for i in range(N)]

wsv.sort(key=lambda x: -(x[0] + x[1]))

MAXD = 0
for a in wsv:
    # print(a)
    MAXD = max(MAXD, a[1])

dp = [-float("inf") for d in range(MAXD + 1)]
ndp = [-float("inf") for d in range(MAXD + 1)]

for i in range(N):
    w, s, v = wsv[i]
    ndp = [-float("inf") for d in range(MAXD + 1)]
    # i番目のブロックを一番下に置くとき
    ndp[s] = max(ndp[s], v)
    for d in range(MAXD + 1):
        # i番目のブロックを取らないとき
        ndp[d] = max(ndp[d], dp[d])
        # i番目のブロックを取るとき
        if d - w >= 0:
            ndp[min(s, d - w)] = max(ndp[min(s, d - w)], dp[d] + v)
    dp = ndp
    # print(dp)

print(max(dp))
