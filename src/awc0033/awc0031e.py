from collections import deque

INF = 10**18


class Edge:
    __slots__ = ("to", "rev", "cap")

    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap


class Dinic:
    __slots__ = ("n", "g", "level")

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.level = [-1] * n

    def add_edge(self, fr, to, cap):
        fwd = Edge(to, len(self.g[to]), cap)
        rev = Edge(fr, len(self.g[fr]), 0)
        self.g[fr].append(fwd)
        self.g[to].append(rev)

    def bfs(self, s, t):
        level = self.level
        for i in range(self.n):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            nv = level[v] + 1
            for e in self.g[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = nv
                    if e.to == t:
                        return True
                    q.append(e.to)
        return level[t] >= 0

    def dfs(self, v, t, f, it):
        if v == t:
            return f
        gv = self.g[v]
        i = it[v]
        while i < len(gv):
            e = gv[i]
            if e.cap > 0 and self.level[e.to] == self.level[v] + 1:
                d = self.dfs(e.to, t, f if f < e.cap else e.cap, it)
                if d:
                    e.cap -= d
                    self.g[e.to][e.rev].cap += d
                    return d
            i += 1
            it[v] = i
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF, it)
                if not f:
                    break
                flow += f
        return flow


N, K, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))
UVC = [list(map(int, input().split())) for i in range(M)]


Q = int(input())
broken = set()

for _ in range(Q):
    S = int(input())
    broken.add(S - 1)
    dinic = Dinic(N + K + 2)
    for u, v, c in UVC:
        dinic.add_edge(u - 1, v - 1, c)
        dinic.add_edge(v - 1, u - 1, c)
    for i in range(K):
        if i in broken:
            continue
        dinic.add_edge(N + K, N + i, W[i])
    for i in range(N):
        dinic.add_edge(i, N + K + 1, B[i])

    res = dinic.max_flow(N + K, N + K + 1)
    print("Yes" if res >= sum(B) else "No")
