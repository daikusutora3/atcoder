from heapq import heappop, heappush


def dijkstra(s, graph, inf=float("inf")):
    """計算量: 時間 O(V + E log(E + 2))、追加空間 O(V + E)。V は頂点数、E は辺数。重みは非負。
    Source: https://github.com/daikusutora3/atcoder
    """
    # 1番コストが低いやつ, 2番目にコストが低いやつ
    dist = [[] for i in range(len(graph))]
    dist[s].append((0, 0))
    # cost, 頂点
    que = [(0, s)]
    while que:
        _cost, v = heappop(que)
        if len(dist[v]) == 0:
            continue
        for to, nc in graph[v]:
            # if len(dist[v]) == 1 and dist[v][0][1] == nc:
            # continue
            if dist[v][0][1] != nc:
                nd = dist[v][0][0] + 1
            elif len(dist[v]) >= 2:
                nd = dist[v][1][0] + 1
            else:
                assert False
            prev = dist[to][:]
            dist[to].append((nd, nc))
            dist[to].sort()
            next = []
            s = set()
            for i in range(len(dist[to])):
                if dist[to][i][1] not in s:
                    s.add(dist[to][i][1])
                    next.append(dist[to][i])
            dist[to] = next
            while len(dist[to]) > 2:
                dist[to].pop()
            if prev != dist[to]:
                heappush(que, (nd, to))
    return dist


N, M = map(int, input().split())
graph = [[] for i in range(N)]
UVC = [list(map(int, input().split())) for i in range(M)]

for i in range(M):
    U, V, C = UVC[i]
    U -= 1
    V -= 1
    graph[U].append((V, C))

dist = dijkstra(0, graph)
if len(dist[N - 1]) == 0:
    print(-1)
else:
    print(dist[N - 1][0][0])
