from functools import lru_cache

N, C = map(int, input().split())
W = list(map(int, input().split()))

dp = [float("inf") for i in range(2**N)]
memo = [-1 for i in range(2**N)]
dp[0] = 0


@lru_cache(maxsize=None)
def set_to_cost(S):
    res = 0
    for i in range(N):
        if S >> i & 1:
            res += W[i]
    return res


for S in range(2**N):
    T = S
    cost = set_to_cost(S)
    if cost <= C:
        dp[S] = min(dp[S], 1)
    while T:
        S_minus_T = S ^ T
        S_minus_T_cost = set_to_cost(S_minus_T)
        if S_minus_T_cost <= C and dp[T] + 1 < dp[S]:
            dp[S] = dp[T] + 1
        T = (T - 1) & S

print(dp[2**N - 1])
