from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)


def solve():
    N, W = map(int, input().split())
    wv = [tuple(map(int, input().split())) for i in range(N)]
    ruiw = [0 for i in range(N + 1)]
    ruiv = [0 for i in range(N + 1)]
    for i in range(N):
        w, v = wv[i]
        ruiw[i + 1] += ruiw[i] + w
        ruiv[i + 1] += ruiv[i] + v

    @lru_cache(maxsize=None)
    def dfs(i, k):
        if i < 0 or k < 0:
            return -float("inf")
        res = 0
        if ruiw[i + 1] <= k:
            res = ruiv[i + 1]
        else:
            res = max(res, dfs(i - 1, k), dfs(i - 1, k - wv[i][0]) + wv[i][1])
        return res

    return dfs(N - 1, W)


T = int(input())
for _ in range(T):
    print(solve())
