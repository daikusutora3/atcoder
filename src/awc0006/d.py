from heapq import heappop, heappush


N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]

LR.sort()
L = [LR[i][0] for i in range(M)]
R = [LR[i][1] for i in range(M)]

if L[0] > 1:
    print(-1)
    exit()

pq = [0]
i = 0
flag = False
ans = -1
while pq:
    v = -heappop(pq)
    ans += 1
    if v == N:
        flag = True
        break
    # 区間が被っているものは入れていく
    while i < M and L[i] <= v + 1:
        heappush(pq, -R[i])
        i += 1

print(ans if flag else -1)
