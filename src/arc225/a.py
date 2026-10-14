import sys

sys.setrecursionlimit(10**6)


N = int(input())
X = [list(map(int, input().split())) for i in range(N)]


ans = [[-1 for j in range(N)] for i in range(N)]


def dfs(i, j):
    global ans, N
    if i < N - 1:
        dfs(i + 1, j)
    elif j < N - 1:
        dfs(0, j + 1)
    else:
        return True
