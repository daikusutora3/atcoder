H, W = map(int, input().split())

grid = [input() for i in range(H)]
dp = [0 for i in range(W)]
dp[0] = 1
mod = 10**9 + 7

for i in range(H):
    # print(f"===={i}====")
    for j in range(W):
        if grid[i][j] == "#":
            dp[j] = 0
            continue
        if j - 1 >= 0:
            # print(f"dp[{j}] += {dp[j - 1]}", end=" ")
            dp[j] += dp[j - 1]
        # print()
        dp[j] %= mod

print(dp[W - 1])
