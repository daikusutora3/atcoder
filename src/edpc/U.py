N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

dp = [0 for i in range(2**N)]

for S in range(2**N):
    # 集合Sに対して初期化
    cost = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (S >> i) & (S >> j) & 1:
                cost += A[i][j]
    dp[S] = cost
    T = S
    while T:
        dp[S] = max(dp[S], dp[T] + dp[S ^ T])
        T = (T - 1) & S


print(dp[2**N - 1])
