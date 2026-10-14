from collections import deque


N = int(input())
S = input()

res = []

cnt = 0
for i in range(N - 1, -1, -1):
    if S[i] == "o":
        cnt += 1
    if cnt % 2 == 1:
        res.append("L")
    else:
        res.append("R")

res.reverse()

ans = deque()

for i, d in enumerate(res):
    if d == "L":
        ans.appendleft(i + 1)
    else:
        ans.append(i + 1)
print(*ans)
