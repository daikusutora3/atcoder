from collections import deque
from itertools import accumulate


def solve():
    N = int(input())
    tree = [[] for i in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
    # ------------------------------------------------------------
    # 0. 根付き木にして、親 par と BFS 順 order と children を作る
    # ------------------------------------------------------------
    par = [-1] * N
    order = []
    children = [[] for _ in range(N)]
    root = 0
    q = deque([root])

    while q:
        u = q.popleft()
        order.append(u)
        for v in tree[u]:
            if v == par[u]:
                continue
            par[v] = u
            children[u].append(v)
            q.append(v)

    # dp[u][v] = 有向辺 u -> v に載せる値
    dp = [{v: 0 for v in adj} for adj in tree]

    # ------------------------------------------------------------
    # 1. bottom-up
    # ------------------------------------------------------------
    for u in reversed(order):
        v = par[u]
        if v == -1:
            continue
        if len(children[u]) == 2:
            dp[u][v] = 1
        elif len(children[u]) >= 3:
            dp[u][v] = 1 + max(
                (dp[x][u] for x in tree[u] if x != v),
                default=0,
            )
        else:
            dp[u][v] = 0

    # ------------------------------------------------------------
    # 2. prefix / suffix
    # ------------------------------------------------------------
    pref = [[] for _ in range(N)]
    suf = [[] for _ in range(N)]

    for u in range(N):
        vals = [dp[v][u] for v in children[u]]
        # pref[u][i] = children[u][:i] から来る最大値
        pref[u] = [0] + list(accumulate(vals, max))
        # suf[u][i+1] = children[u][i+1:] から来る最大値
        suf[u] = list(accumulate(reversed(vals), max))[::-1] + [0]

    # ------------------------------------------------------------
    # 3. top-down
    # ------------------------------------------------------------
    for u in order:
        p = par[u]
        par_in = dp[p][u] if p != -1 else 0
        for i, v in enumerate(children[u]):
            if len(children[u]) - 1 + (1 if p != -1 else 0) == 2:
                dp[u][v] = 1
            elif len(children[u]) - 1 + (1 if p != -1 else 0) >= 3:
                dp[u][v] = 1 + max(par_in, pref[u][i], suf[u][i + 1])
            else:
                dp[u][v] = 0
    ans = 0
    for v in range(N):
        kouho = []
        for x in tree[v]:
            kouho.append(dp[x][v])
        kouho.sort()
        if len(kouho) >= 4:
            ans = max(ans, kouho[-1] + kouho[-2] + 1)
        elif len(kouho) == 3:
            ans = max(ans, kouho[-1] + 1)
        elif len(kouho) == 2:
            ans = max(ans, 1)
    return ans


Q = int(input())
for _ in range(Q):
    print(solve())
