from collections import deque

from atcoder.dsu import DSU


def solve():
    N, M = map(int, input().split())
    color = [[0, 0, 0] for i in range(N)]
    dsu = [DSU(N), DSU(N), DSU(N)]
    for _ in range(M):
        u, v, l = map(int, input().split())
        u -= 1
        v -= 1
        l -= 1
        dsu[l].merge(u, v)
        color[u][l] = 1
        color[v][l] = 1
    seen = {}
    for i in range(N):
        pair = (dsu[1].leader(i), dsu[2].leader(i))
        if pair not in seen:
            seen[pair] = i
        else:
            dsu[0].merge(seen[pair], i)
    ans = []
    for i in range(N):
        if dsu[0].leader(0) == dsu[0].leader(i):
            ans.append(i + 1)
    ans.sort()
    print(len(ans))
    print(*ans)


T = int(input())
for _ in range(T):
    solve()
