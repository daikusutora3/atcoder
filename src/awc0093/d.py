from collections import deque


INF = 10**9 + 10


N, M, K = map(int, input().split())
H = list(map(int, input().split()))
UV = [list(map(int, input().split())) for i in range(M)]
UV = [[u - 1, v - 1] for u, v in UV]


ban = set()
graph = [[] for i in range(N)]
for u, v in UV:
    graph[u].append((v, 1))
    graph[v].append((u, 1))


def bfs(s, graph, inf=INF):
    global ban
    dist = [inf] * len(graph)
    dist[s] = 0
    que = deque([(0, s)])
    while que:
        cost, v = que.popleft()
        if cost != dist[v]:
            continue
        for to, w in graph[v]:
            nd = cost + w
            if nd < dist[to] and to not in ban:
                dist[to] = nd
                que.append((nd, to))
    return dist


def is_ok(k):
    global N, M, K, H, UV, ban
    ban = set()
    for i in range(N):
        if H[i] > k:
            ban.add(i)
    dist = bfs(0, graph)
    return dist[N - 1] + 1 <= K


ok = INF
ng = max(H[0], H[-1]) - 1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid


print(-1 if ok == INF else ok)
