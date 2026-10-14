N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]
mod = 10**9 + 7

dp = [0 for _ in range(2**N)]
dp[0] = 1

S = [set() for i in range(N)]

for bit in range(2**N):
    bl = bit.bit_count()
    for i in range(N):
        if bit >> i & 1 and A[bl - 1][i]:
            dp[bit] += dp[bit ^ (1 << i)]
            dp[bit] %= mod

print(dp[2**N - 1])
