from collections import deque


def bfs(graph, starts, visited=None):
    """重みなしグラフで starts 内の最も近い始点からの距離を返す。

    計算量: 時間 O(V + E + K)、追加空間 O(V)。
    V は頂点数、E は隣接リストの要素数、K は starts の要素数（重複を含む）。
    始点の距離は 0、到達不能な頂点は -1。starts が空なら全頂点 -1。
    visited は長さ V の bool 配列。True の頂点は始点でも除外し、距離は -1。
    渡された配列を直接更新する。省略時は呼び出しごとに新規作成する。

    Source: https://github.com/daikusutora3/atcoder
    """
    if visited is None:
        visited = [False] * len(graph)
    dist = [-1] * len(graph)
    que = deque()
    for s in starts:
        if not visited[s]:
            visited[s] = True
            dist[s] = 0
            que.append(s)

    while que:
        v = que.popleft()
        for to in graph[v]:
            if visited[to]:
                continue
            visited[to] = True
            dist[to] = dist[v] + 1
            que.append(to)

    return dist


gaitou = [2, 6, 10, 13, 18, 22, 26]
A = [
    12,
    5,
    20,
    0,
    7,
    15,
    3,
    25,
    8,
    1,
    30,
    6,
    14,
    2,
    18,
    10,
    4,
    22,
    9,
    13,
    0,
    16,
    11,
    27,
    5,
    19,
    2,
    24,
    7,
    21,
]

N = len(A)
graph = [[] for i in range(N)]

for i in range(N):
    if i + 1 < N:
        graph[i].append(i + 1)
    if i - 1 >= 0:
        graph[i].append(i - 1)


dist = bfs(graph, gaitou)

ans = []
for i in range(N):
    ans.append(dist[i] * A[i])

print(ans)
