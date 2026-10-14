N = int(input())

XY = [list(map(int, input().split())) for i in range(N)]

dp = [[float("inf") for __ in range(N)] for _ in range(2**N)]


for i in range(1, N):
    dp[1 << i][i] = (XY[0][0] - XY[i][0]) ** 2 + (XY[0][1] - XY[i][1]) ** 2
for bit in range(0, 2**N):
    for i in range(N):
        for j in range(N):
            # i番目のbitが立っていますか？(もう行ったことがあるから)
            # j番目のbitは立っていないですよね？(今から行くから)
            if (bit >> i & 1) and not (bit >> j & 1):
                # bitの中でj番目を1にする
                dp[bit | 1 << j][j] = min(
                    dp[bit | 1 << j][j],
                    dp[bit][i]
                    + (XY[j][0] - XY[i][0]) ** 2
                    + (XY[j][1] - XY[i][1]) ** 2,
                )


print(dp[2**N - 1][0])
