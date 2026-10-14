from heapq import heappop, heappush


N, D = map(int, input().split())


sque = []
tque = []
for i in range(N):
    S, T = map(int, input().split())
    heappush(sque, (S, i))
    heappush(tque, (T, i))


ans = 0
jotai = [2 for i in range(N)]
cnt = 0
while len(tque) and tque[0][0] < D:
    _, i = heappop(tque)
    jotai[i] -= 2
for x in range(10**6 + 1):
    while len(sque) and sque[0][0] == x:
        _, i = heappop(sque)
        jotai[i] += 1
        if jotai[i] == 3:
            cnt += 1
    ans += (cnt * (cnt - 1)) // 2
    while len(tque) and tque[0][0] == x + D:
        _, i = heappop(tque)
        if jotai[i] == 3:
            cnt -= 1
        jotai[i] -= 2


print(ans)
