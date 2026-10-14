from collections import deque
import heapq

N, M = map(int, input().split())
HS = [list(map(int, input().split())) for i in range(N)]
P = list(map(int, input().split()))
P.sort()
HS.sort()
HS = deque(HS)

hq = []
ans = 0
flag = True
for p in P:
    while HS and HS[0][0] <= p:
        heapq.heappush(hq, -HS.popleft()[1])
    if len(hq) == 0:
        flag = False
        break
    else:
        ans -= heapq.heappop(hq)

print(ans if flag else -1)
