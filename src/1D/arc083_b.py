from heapq import heapify, heappop

N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

pq = []
for i in range(N):
    for j in range(i + 1, N):
        pq.append((A[i][j], i, j))

heapify(pq)

flag = True
ans = 0
while pq:
    cost, i, j = heappop(pq)
    is_ok = False
    for k in range(N):
        if k == i or k == j:
            continue
        if A[i][k] + A[k][j] < cost:
            flag = False
            break
        elif A[i][k] + A[k][j] == cost:
            # 辺を引かなくても良いよ
            is_ok = True
    if not is_ok:
        ans += cost
    if not flag:
        break

if flag:
    print(ans)
else:
    print(-1)
