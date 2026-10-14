from collections import deque

from atcoder.dsu import DSU

N, Q = map(int, input().split())
graph = [[] for i in range(N)]
queries = [list(input().split()) for i in range(Q)]
dsu_all = DSU(N)

mod = 998244353
sinkoku = []

for q in range(Q):
    if queries[q][0] == "A":
        u, v, c = queries[q][1:]
        u, v = int(u) - 1, int(v) - 1

        iu = len(graph[u])
        iv = len(graph[v])

        sinkoku.append([u, v, c, iu, iv])

        dsu_all.merge(u, v)
        graph[u].append((v, c))
        graph[v].append((u, c))

    elif queries[q][0] == "R":
        k = int(queries[q][1]) - 1

        c = sinkoku[k][2]
        nc = "X" if c == "X" else str(int(c) ^ 1)

        u, v, _, iu, iv = sinkoku[k + 1]

        sinkoku[k + 1][2] = nc
        graph[u][iu] = (v, nc)
        graph[v][iv] = (u, nc)

    # 違反していないかのチェック + 連結成分の計算
    color = [-1 for i in range(N)]
    cnt = 0
    flag = True

    for i in range(N):
        if color[i] != -1:
            continue

        cnt += 1
        queue = deque([i])
        color[i] = 0

        while len(queue):
            v = queue.popleft()

            for u, c in graph[v]:
                if c == "X":
                    continue
                elif color[u] == -1:
                    queue.append(u)
                    color[u] = color[v] if c == "0" else (color[v] ^ 1)
                elif c == "0" and color[v] != color[u]:
                    flag = False
                elif c == "1" and color[v] == color[u]:
                    flag = False

    if flag:
        print(pow(2, cnt - len(dsu_all.groups()), mod))
    else:
        print(0)
