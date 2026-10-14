from collections import deque


s = input()
t = input()

dp = [-float("inf") for i in range((len(s) + 1) * (len(t) + 1))]

# 0: 上
# 1: 左from collections import deque


s = input()
t = input()

dp = [-float("inf") for i in range((len(s) + 1) * (len(t) + 1))]

# 0: 上
# 1: 左
# 2: 左上
memo = [-1 for i in range((len(s) + 1) * (len(t) + 1))]
dp[0] = 0

direction = {0: [-1, 0], 1: [0, -1], 2: [-1, -1]}


def ind(i, j):
    global s, t
    return i + j * (len(s) + 1)


def chmax(i, j, x, d):
    global dp, memo
    if dp[ind(i, j)] < x:
        dp[ind(i, j)] = x
        memo[ind(i, j)] = d


for i in range(len(s) + 1):
    for j in range(len(t) + 1):
        if 1 <= i <= len(s) and 1 <= j <= len(t) and s[i - 1] == t[j - 1]:
            chmax(i, j, dp[ind(i - 1, j - 1)] + 1, 2)
        if i - 1 >= 0:
            chmax(i, j, dp[ind(i - 1, j)], 0)
        if j - 1 >= 0:
            chmax(i, j, dp[ind(i, j - 1)], 1)

ans = deque()
i, j = len(s), len(t)
while i != 0 and j != 0:
    d = memo[ind(i, j)]
    di, dj = direction[d]
    ni, nj = i + di, j + dj
    if i - 1 == ni and j - 1 == nj:
        ans.appendleft(s[ni])
    i, j = ni, nj

print("".join(ans))

# 2: 左上
memo = [-1 for i in range((len(s) + 1) * (len(t) + 1))]
dp[0] = 0

direction = {0: [-1, 0], 1: [0, -1], 2: [-1, -1]}


def ind(i, j):
    global s, t
    return i + j * (len(s) + 1)


def chmax(i, j, x, d):
    global dp, memo
    if dp[ind(i, j)] < x:
        dp[ind(i, j)] = x
        memo[ind(i, j)] = d


for i in range(len(s) + 1):
    for j in range(len(t) + 1):
        if 1 <= i <= len(s) and 1 <= j <= len(t) and s[i - 1] == t[j - 1]:
            chmax(i, j, dp[ind(i - 1, j - 1)] + 1, 2)
        if i - 1 >= 0:
            chmax(i, j, dp[ind(i - 1, j)], 0)
        if j - 1 >= 0:
            chmax(i, j, dp[ind(i, j - 1)], 1)

ans = deque()
i, j = len(s), len(t)
while i != 0 and j != 0:
    d = memo[ind(i, j)]
    di, dj = direction[d]
    ni, nj = i + di, j + dj
    if i - 1 == ni and j - 1 == nj:
        ans.appendleft(s[ni])
    i, j = ni, nj

print("".join(ans))
