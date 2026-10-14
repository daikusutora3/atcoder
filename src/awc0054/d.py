import itertools


N = int(input())
A = list(map(int, input().split()))
dp = [[0] * (N + 1) for l in range(N + 1)]

ruiseki = list(itertools.accumulate(A))
for length in range(1, N + 1):
    for l in range(N - length + 1):
        r = l + length - 1
        s = ruiseki[r] - (ruiseki[l - 1] if l - 1 >= 0 else 0)
        dp[l][r] = s - min(dp[l + 1][r], dp[l][r - 1])

tak = dp[0][N - 1]
aok = ruiseki[-1] - tak
print(tak, aok)
