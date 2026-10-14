from collections import deque


N, S = map(int, input().split())
dp = [[False for j in range(S + 1)] for i in range(N + 1)]
dp[0][0] = True
AB = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    a, b = AB[i]
    for s in range(S + 1):
        if s - a >= 0 and dp[i][s - a]:
            dp[i + 1][s] = True
        if s - b >= 0 and dp[i][s - b]:
            dp[i + 1][s] = True

if dp[N][S]:
    ans = deque([])
    now = [N, S]
    for _ in range(N):
        i, s = now
        a, b = AB[i - 1]
        if s - a >= 0 and dp[i - 1][s - a]:
            ans.appendleft("A")
            now = [i - 1, s - a]
        elif s - b >= 0 and dp[i - 1][s - b]:
            ans.appendleft("B")
            now = [i - 1, s - b]
    print("".join(ans))
else:
    print("Impossible")
