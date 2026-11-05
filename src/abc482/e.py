from collections import defaultdict, deque

N = int(input())
tree = [[] for i in range(2 * N - 1)]
for i in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    tree[u].append(N + i)
    tree[N + i].append(u)
    tree[v].append(N + i)
    tree[N + i].append(v)
C = list(map(int, input().split()))

queue = deque([0])
seen = [0 for i in range(2 * N - 1)]
v = 0
while queue:
    v = queue.popleft()
    seen[v] = 1
    for nv in tree[v]:
        if seen[nv] == 0:
            queue.append(nv)
            seen[nv] = 1


def tree_diameter(graph):
    """重みなし無向木の直径を (辺数, 両端を含む頂点列) で返す。

    計算量: 時間 O(N)、追加空間 O(N)。N は頂点数。
    空でない連結な単純無向木を渡す。直径が複数ならいずれか1本を返す。

    Source: https://github.com/daikusutora3/atcoder
    """

    def search(s):
        """始点からの最遠頂点・距離配列・親配列を時間 O(N)、空間 O(N) で求める。"""
        dist = [-1] * len(graph)
        parent = [-1] * len(graph)
        dist[s] = 0
        que = deque([s])
        v = s
        while que:
            v = que.popleft()
            for to in graph[v]:
                if dist[to] != -1:
                    continue
                dist[to] = dist[v] + 1
                parent[to] = v
                que.append(to)
        return v, dist, parent

    s, _, _ = search(0)
    t, dist, parent = search(s)
    path = []
    v = t
    while v != -1:
        path.append(v)
        v = parent[v]
    path.reverse()
    return dist[t], path


dia, path = tree_diameter(tree)
center = path[dia // 2 : dia // 2 + 1 + dia % 2][0]

queue = deque([[center, 0]])
colors = defaultdict(int)
seen = [0 for i in range(2 * N - 1)]
while queue:
    v, cost = queue.popleft()
    seen[v] = 1
    for nv in tree[v]:
        if seen[nv] == 0:
            queue.append([nv, cost + 1])
            seen[nv] = 1
    if cost == dia // 2:
        colors[C[v] - 1] += 1

ans = 0
v_colors = defaultdict(int)
seen = [0 for i in range(2 * N - 1)]
seen[center] = 1
for v in tree[center]:
    queue = deque([[v, 0]])
    while queue:
        v, cost = queue.popleft()
        seen[v] = 1
        for nv in tree[v]:
            if seen[nv] == 0:
                queue.append([nv, cost + 1])
                seen[nv] = 1
        if cost == dia // 2 - 1:
            v_colors[C[v] - 1] += 1
    for c in v_colors:
        ans += (colors[c] - v_colors[c]) * v_colors[c]
    v_colors = defaultdict(int)

print(ans // 2)
