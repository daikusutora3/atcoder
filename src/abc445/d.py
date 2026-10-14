from collections import defaultdict


H, W, N = map(int, input().split())
HW = [list(map(int, input().split())) for i in range(N)]
ans = defaultdict()

h_pieace = defaultdict(set)
w_pieace = defaultdict(set)

for i in range(N):
    h, w = HW[i]
    h_pieace[h].add(i)
    w_pieace[w].add(i)

now = [1, 1]
ans = defaultdict()
for _ in range(N):
    if h_pieace[H]:
        id = h_pieace[H].pop()
        h, w = HW[id]
        w_pieace[w].remove(id)
        ans[id] = now
        now = [now[0], now[1] + w]
        W = W - w
    elif w_pieace[W]:
        id = w_pieace[W].pop()
        h, w = HW[id]
        h_pieace[h].remove(id)
        ans[id] = now
        now = [now[0] + h, now[1]]
        H = H - h

for i in range(N):
    print(*ans[i])
