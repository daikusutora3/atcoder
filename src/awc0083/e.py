N, K = map(int, input().split())
P = list(map(int, input().split()))

C = [list(map(int, input().split())) for i in range(N)]

# dp[r][bit]
# r: 右端に選んだ宝石
# bit: 今まで選んだ宝石のbit
dp = [[-float("inf") for bit in range(2**N)] for r in range(N)]


for i in range(N):
    dp[i][1 << i] = P[i]

ans = -float("inf")
for bit in range(1, 2**N):
    cnt = bit.bit_count()
    if cnt > K:
        continue
    st = -1
    for i in range(N):
        if (bit >> i) & 1:
            st = i
            break
    for r in range(N):
        if not ((bit >> r) & 1):
            continue
        if cnt >= 2 and r == st:
            continue

        for br in range(N):
            if (bit >> br) & 1:
                dp[r][bit] = max(dp[r][bit], dp[br][bit ^ (1 << r)] + C[br][r] + P[r])
        if bit.bit_count() == K:
            ans = max(ans, dp[r][bit] + C[r][st])

print(ans)
