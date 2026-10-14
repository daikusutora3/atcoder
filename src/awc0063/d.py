N = int(input())
V = list(map(int, input().split()))

rui = [0 for i in range(N + 1)]
for i in range(N):
    rui[i + 1] = rui[i] + V[i]
# 長さk: 1~Nに計算をする
# l, r: [l, r)における最適値
dp = [[-float("inf") for r in range(N + 1)] for l in range(N + 1)]
for l in range(N + 1):
    dp[l][l] = 0

for k in range(1, N + 1):
    for l in range(N):
        r = l + k
        if r > N:
            break
        s = rui[r] - rui[l]
        # 右端を取る時
        dp[l][r] = max(dp[l][r], s - dp[l][r - 1])
        # 左端を取る時
        dp[l][r] = max(dp[l][r], s - dp[l + 1][r])

print(dp[0][N] - (rui[N] - dp[0][N]))
