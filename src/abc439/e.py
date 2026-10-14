import bisect


def lis(a, inf=1e18):
    n = len(a)
    dp = [inf] * n
    for i in range(n):
        pos = bisect.bisect_left(dp, a[i])
        dp[pos] = a[i]
    return bisect.bisect_left(dp, inf)


N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

s = set()
AB.sort(key=lambda x: (x[0], -x[1]))
print(lis([ab[1] for ab in AB]))
