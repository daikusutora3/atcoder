from collections import deque
from heapq import heappop, heappush


N, K, Q = map(int, input().split())
A = list(map(int, input().split())) + [-1]

ans = float("inf")

for mi in set(A):
    simas = []
    sima = []
    for i in range(N + 1):
        if A[i] >= mi:
            sima.append(A[i])
        else:
            if len(sima) >= K:
                simas.append(sima)
            sima = []
    kouho = []
    for i, sima in enumerate(simas):
        sima.sort()
        simas[i] = deque(sima)
        heappush(kouho, (sima[0], i))
    cnt = 0
    ma = 0
    while cnt < Q and len(simas) and len(kouho):
        v, i = heappop(kouho)
        ma = max(ma, v)
        simas[i].popleft()
        if len(simas[i]) < K:
            pass
        else:
            heappush(kouho, (simas[i][0], i))
        cnt += 1
    if cnt == Q:
        ans = min(ans, ma - mi)

print(ans)
