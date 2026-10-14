from heapq import heapify, heappop, heappush


N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]

LR.sort()

# ここには左端優先でpushしていく
pq = []
heapify(pq)
i = 0
flag = True
for x in range(1, N + 1):
    while i < M and LR[i][0] <= x:
        heappush(pq, LR[i][1])
        i += 1
    if len(pq) == 0:
        continue
    if pq[0] >= x:
        heappop(pq)
    elif pq[0] < x:
        flag = False

print("Yes" if flag and len(pq) == 0 else "No")
