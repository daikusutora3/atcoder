from collections import deque


N, K = map(int, input().split())

V = list(map(int, input().split()))

queue = deque()

r = 0
now = 0
ans = 0
for l in range(N):
    while len(queue) and queue[0] < l:
        now -= V[queue.popleft()]
    while now < K and r < N:
        now += V[r]
        queue.append(r)
        r += 1
    # print(f"{l}~{r}: {now}")
    if now >= K:
        ans += N - r + 1

print(ans)
