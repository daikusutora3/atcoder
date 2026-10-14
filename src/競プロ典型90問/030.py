from collections import deque

N, K = map(int, input().split())

pl = []  # 発見した素数のリスト
lpf = [None] * (N + 1)  # 発見した最小素因数。
for d in range(2, N + 1):
    if lpf[d] is None:
        lpf[d] = d
        pl.append(d)
    for p in pl:
        if p * d > N or p > lpf[d]:
            break
        lpf[p * d] = p

seen = [False for i in range(N + 1)]
ans = 0

queue = deque([(1, 0)])

while queue:
    cur, size = queue.popleft()
    if size >= K:
        ans += 1
    for p in pl:
        if cur * p > N:
            break
        if not seen[cur * p]:
            if N // 2 < cur * p and K - size >= 2:
                continue
            queue.append((cur * p, size + 1 if cur % p > 0 else size))
            seen[cur * p] = True


print(ans)
