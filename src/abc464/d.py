def solve():
    N = int(input())
    S = input()
    X = list(map(int, input().split()))
    Y = [0] + list(map(int, input().split()))
    # dp[i][0] i番目がSの時のi番目までにおける幸福度の最大
    # dp[i][1] i番目がRの時のi番目までにおける幸福度の最大
    dp = [[-float("inf"), -float("inf")] for i in range(N + 1)]
    dp[0] = [0, 0]
    for i in range(N):
        # i+1日目に晴れ
        dp[i + 1][0] = max(
            dp[i + 1][0],
            dp[i][0] - (X[i] if S[i] == "R" else 0),
            dp[i][1] - (X[i] if S[i] == "R" else 0) + Y[i],
        )
        # i日目に雨
        dp[i + 1][1] = max(
            dp[i + 1][1],
            dp[i][0] - (X[i] if S[i] == "S" else 0),
            dp[i][1] - (X[i] if S[i] == "S" else 0),
        )
    print(max(dp[N]))


T = int(input())
for _ in range(T):
    solve()
