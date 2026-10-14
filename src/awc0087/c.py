from collections import deque


N, K = map(int, input().split())

A = list(map(int, input().split()))

queue = deque()
now = 0


def diff_height(i, j):
    global A
    return abs(A[i] - A[j])


ans = float("inf")

for r in range(N):
    if len(queue):
        now += diff_height(r, queue[-1])
    queue.append(r)
    while len(queue) > 2 and now - diff_height(queue[0], queue[1]) >= K:
        now -= diff_height(queue[0], queue[1])
        queue.popleft()
    if now >= K:
        ans = min(ans, len(queue))

print(-1 if ans == float("inf") else ans)
