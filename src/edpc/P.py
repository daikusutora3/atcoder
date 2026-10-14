from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)


N = int(input())
mod = 10**9 + 7
tree = [[] for i in range(N)]

for _ in range(N - 1):
    x, y = map(int, input().split())
    tree[x - 1].append(y - 1)
    tree[y - 1].append(x - 1)


# v: ある頂点v
# p: vの親の頂点
# color: 頂点vの色
@lru_cache(maxsize=None)
def dfs(v, p, color):
    global tree, mod
    res = 1
    for u in tree[v]:
        if u == p:
            continue
        res *= dfs(u, v, 0) + (0 if color == 1 else dfs(u, v, 1))
        res %= mod
    return res


print((dfs(0, -1, 0) + dfs(0, -1, 1)) % mod)
