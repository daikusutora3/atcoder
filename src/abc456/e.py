def has_directed_cycle(graph, starts=None):
    n = len(graph)

    # 0: 未訪問
    # 1: 訪問中
    # 2: 探索完了
    state = [0] * n

    if starts is None:
        starts = range(n)

    for s in starts:
        if state[s] != 0:
            continue

        state[s] = 1
        stack = [[s, 0]]

        while stack:
            v, idx = stack[-1]

            if idx == len(graph[v]):
                state[v] = 2
                stack.pop()
                continue

            to = graph[v][idx]
            stack[-1][1] += 1

            if state[to] == 0:
                state[to] = 1
                stack.append([to, 0])
            elif state[to] == 1:
                return True
    return False


def solve():
    N, M = map(int, input().split())
    UV = [list(map(int, input().split())) for i in range(M)]
    W = int(input())
    S = [input() for i in range(N)]
    graph = [[] for i in range(N * W)]
    for _ in range(M):
        u, v = UV[_]
        u, v = u - 1, v - 1
        for w in range(W):
            bw = (w - 1) % W
            if S[u][bw] == "o" and S[v][w] == "o":
                graph[u + bw * N].append(v + w * N)
            if S[v][bw] == "o" and S[u][w] == "o":
                graph[v + bw * N].append(u + w * N)
    for i in range(N):
        for w in range(W):
            bw = (w - 1) % W
            if S[i][bw] == "o" and S[i][w] == "o":
                graph[i + bw * N].append(i + w * N)

    cycle = has_directed_cycle(graph)
    print("Yes" if cycle else "No")


T = int(input())

for _ in range(T):
    solve()
