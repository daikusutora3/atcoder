from collections import deque


N, M = map(int, input().split())
XC = [list(map(int, input().split())) for i in range(N)]

ans = 0
now_C = 0
queue = deque()
for r in range(N):
    queue.append(XC[r])
    now_C += XC[r][1]
    while now_C > M:
        x, c = queue.popleft()
        now_C -= c
    if len(queue):
        ans = max(ans, XC[r][0] - queue[0][0])

print(ans)
