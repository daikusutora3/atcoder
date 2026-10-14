import sys

sys.setrecursionlimit(10**6)

N = int(input())

beki = []
now = 1
while now <= 10**9:
    beki.append(str(now))
    now *= 2

ans = []


def dfs(s):
    for b in beki:
        if len(s) + len(b) <= 9:
            t = s + b
            ans.append(t)
            dfs(t)


dfs("")

ans = list(set([int(a) for a in ans]))
ans.sort()
print(ans[N - 1])
