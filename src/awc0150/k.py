N, M, K = map(int, input().split())
graph = [[] for i in range(N)]

ans = float("inf")
for _ in range(M):
    U, V, W = map(int, input().split())
    U -= 1
    V -= 1
    graph[U].append((V, W))
    graph[V].append((U, W))

for edge in graph:
    edge.sort(key=lambda x: x[1])

# うにグラフ (k <= 3以下なら全てこれで対応できる)
for v in range(N):
    if not (len(graph[v]) >= K - 1):
        continue
    ans = min(ans, sum([graph[v][i][1] for i in range(K - 1)]))

# K == 4 or 5のときはパスである可能性が出てくる
if K == 4:
    for v1 in range(N):
        for v2, a in graph[v1]:
            for v3, b in graph[v2][:3]:
                for v4, c in graph[v3][:3]:
                    if len({v1, v2, v3, v4}) == 4:
                        ans = min(ans, a + b + c)

if K == 5:
    # パス
    for v1 in range(N):
        for v2, a in graph[v1]:
            for v3, b in graph[v1]:
                for v4, c in graph[v2][:4]:
                    for v5, d in graph[v3][:4]:
                        if len({v1, v2, v3, v4, v5}) == 5:
                            ans = min(ans, a + b + c + d)
    # 長さ4のパスに突起が1個ついてるやつ
    for v1 in range(N):
        for v2, a in graph[v1][:4]:
            for v3, b in graph[v1][:4]:
                for v4, c in graph[v1]:
                    for v5, d in graph[v4][:4]:
                        if len({v1, v2, v3, v4, v5}) == 5:
                            ans = min(ans, a + b + c + d)


print(ans)
