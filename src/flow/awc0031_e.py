from atcoder.maxflow import MFGraph

N, K, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

UVC = [list(map(int, input().split())) for i in range(M)]

Q = int(input())
broken = set()
for _ in range(Q):
    S = int(input())
    broken.add(S - 1)
    # 0~N-1: 工場頂点
    # N~N+K-1: 発電所頂点
    # N+K: 始点
    # N+K+1: 終点
    graph = MFGraph(N + K + 2)
    for u, v, c in UVC:
        u -= 1
        v -= 1
        graph.add_edge(v, u, c)
        graph.add_edge(u, v, c)
    for k in range(K):
        if k in broken:
            continue
        graph.add_edge(N + K, N + k, W[k])
    for i in range(N):
        graph.add_edge(i, N + K + 1, B[i])
    res = graph.flow(N + K, N + K + 1)
    if res >= sum(B):
        print("Yes")
    else:
        print("No")
