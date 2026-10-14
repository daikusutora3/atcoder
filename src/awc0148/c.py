N, T, S = map(int, input().split())

INF = float("inf")

dp = [-INF for i in range(T - S + 1)]
ndp = [-INF for i in range(T - S + 1)]
dp[0] = 0

for i in range(N):
    C, P = map(int, input().split())
    for j in range(T - S + 1):
        if j - C >= 0:
            ndp[j] = max(ndp[j], dp[j - C] + P)
        ndp[j] = max(ndp[j], dp[j])
    dp = ndp
    ndp = [-INF for i in range(T - S + 1)]

print(max(dp))
