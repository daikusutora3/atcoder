import sys

sys.setrecursionlimit(10**6)
N, K = map(int, input().split())

ok = [[False for j in range(K + 1)] for i in range(N + 1)]
for i in range(N + 1):
    ok[N][0] = True

for i in range(N - 1, -1, -1):
    is_ok = [False for i in range(i + 1)]
    for j in range(K + 1):
        is_ok[j % (i + 1)] |= ok[i + 1][j]
        ok[i][j] |= is_ok[j % (i + 1)]

A = [-1 for i in range(N)]


def dfs(i, k):
    global N, ok, A
    if 0 < k < i or not ok[i][k]:
        return
    if i == N - 1:
        if k % (i + 1) == 0:
            A[-1] = k // (i + 1)
            print(*A)
        return

    for j in range(k // (i + 1) + 1):
        nk = k - j * (i + 1)
        if nk < 0:
            break
        A[i] = j
        dfs(i + 1, nk)
    return


if N == 1:
    print(K)
else:
    for a in range(K + 1):
        A[0] = a
        dfs(1, K - a)
