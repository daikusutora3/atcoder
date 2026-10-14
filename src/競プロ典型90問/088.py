import sys

sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
A = list(map(int, input().split()))
graph = [[] for i in range(N)]

for _ in range(Q):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)


seen = [False for i in range(8890)]
ans = [0 for i in range(8890)]

# print(graph)


def ban(v, banned):
    global graph
    nbanned = banned
    for u in graph[v]:
        nbanned |= 1 << u
    return nbanned


# print(bin(ban(1, 0)))


def dfs(i, sum, chosen, banned):
    global seen
    for j in range(i + 1, N):
        if (banned >> j) & 1:
            continue
        nbanned = ban(j, banned)
        nchosen = chosen | (1 << j)
        nsum = sum + A[j]

        # 答えを出すだけ！！
        if seen[nsum]:
            print(ans[nsum].bit_count())
            res = []
            for k in range(N):
                if (ans[nsum] >> k) & 1:
                    res.append(k + 1)
            print(*res)
            print(nchosen.bit_count())
            res = []
            for k in range(N):
                if (nchosen >> k) & 1:
                    res.append(k + 1)
            print(*res)
            exit()

        seen[nsum] = True
        ans[nsum] = nchosen
        dfs(j, nsum, nchosen, nbanned)


dfs(-1, 0, 0, 0)
