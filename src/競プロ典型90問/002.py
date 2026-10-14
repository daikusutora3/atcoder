import sys

sys.setrecursionlimit(10**6)

N = int(input())

ans = set()


def dfs(s, cnt, length):
    global N, ans
    if length == N:
        if cnt == 0:
            ans.add(s)
        return
    if cnt <= 0:
        dfs(s + "(", cnt + 1, length + 1)
    else:
        dfs(s + "(", cnt + 1, length + 1)
        dfs(s + ")", cnt - 1, length + 1)


dfs("", 0, 0)
if ans:
    print(*sorted(list(ans)), sep="\n")
