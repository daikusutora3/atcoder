N, S = map(int, input().split())

dp = [-float("inf") for _ in range(S + 1)]
dp[0] = 0
ndp = [-float("inf") for _ in range(S + 1)]


def f(x):
    now = 1
    res = []
    while x > 0:
        now = min(x, now)
        x -= now
        res.append(now)
        now *= 2
    return res


for i in range(N):
    W, V, C = map(int, input().split())
    for c in f(C):
        ndp = [-float("inf") for _ in range(S + 1)]
        for s in range(S + 1):
            ndp[s] = max(ndp[s], dp[s])
            if s - W * c >= 0:
                ndp[s] = max(ndp[s], dp[s - c * W] + V * c)
        dp = ndp

print(dp[S] if dp[S] != -float("inf") else -1)
