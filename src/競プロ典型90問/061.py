from collections import deque


Q = int(input())
dq = deque()

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        dq.append(x)
    elif t == 2:
        dq.appendleft(x)
    else:
        print(dq[-x])
