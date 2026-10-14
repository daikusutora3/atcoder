import sys

sys.setrecursionlimit(10**6)


def dfs(graph, v, p, color: list):
    res = -1
    for nv in graph[v]:
        if nv == p:
            continue
        if color[nv] != -1:
            if color[v] == color[nv]:
                res = [nv, v]
                return res
            continue
        color[nv] = (color[v] + 1) % 2
        result = dfs(graph, nv, v, color)
        if result != -1:
            result.append(v)
            return result
    return res


def solve():
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    color = [-1 for i in range(N)]
    color[0] = 0
    ans = dfs(graph, 0, -1, color)
    if ans == -1:
        print(ans)
    else:
        i = 1
        for j in range(1, len(ans)):
            if ans[j] == ans[0]:
                i = j
                break
        ans = [a + 1 for a in ans[:i]]
        print(len(ans))
        print(*ans)


T = int(input())
for _ in range(T):
    solve()
