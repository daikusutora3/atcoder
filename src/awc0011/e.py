from collections import deque

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]

dp = [[0 for j in range(M + 1)] for i in range(N + 1)]
memo = [[[] for j in range(M + 1)] for i in range(N + 1)]
for i in range(1, N + 1):
    A, B = AB[i - 1]
    for w in range(M + 1):
        dp[i][w] = max(dp[i][w], dp[i - 1][w])
        memo[i][w].append((i - 1, w))
        if 0 <= w - A:
            if dp[i][w] < dp[i - 1][w - A] + B:
                memo[i][w] = [(i - 1, w - A)]
            elif dp[i][w] == dp[i - 1][w - A] + B:
                memo[i][w].append((i - 1, w - A))
            dp[i][w] = max(dp[i][w], dp[i - 1][w - A] + B)


flag = ["No" for i in range(N + 1)]

ans = max(dp[N])

queue = deque()

for w in range(M + 1):
    if dp[N][w] == ans:
        queue.append([N, w])

seen = [[False for j in range(M + 1)] for i in range(N + 1)]
while queue:
    i, w = queue.popleft()
    for ni, nw in memo[i][w]:
        if w != nw:
            flag[i] = "Yes"
        if not seen[ni][nw]:
            queue.append([ni, nw])
        seen[ni][nw] = True

for i in range(N):
    print(flag[i + 1])
