N, K = map(int, input().split())

A = list(map(int, input().split()))
dp = [False for _ in range(K + 1)]

for k in range(K + 1):
    for a in A:
        if k - a >= 0:
            dp[k] |= not dp[k - a]

print("First" if dp[K] else "Second")
