import sys

sys.setrecursionlimit(10**6)


N = int(input())
a = list(map(int, input().split()))

memo = [[-float("inf") for r in range(N + 1)] for l in range(N + 1)]


def dfs(l, r):
    global a, memo
    if memo[l][r] != -float("inf"):
        return memo[l][r]
    if l > r:
        memo[l][r] = 0
        return memo[l][r]
    res = -float("inf")
    res = max(res, a[l] + -dfs(l + 1, r))
    res = max(res, -dfs(l, r - 1) + a[r])
    memo[l][r] = res
    return res


# print(memo)

print(dfs(0, N - 1))
