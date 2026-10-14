from collections import deque

N, M, K = map(int, input().split())

A = list(map(int, input().split()))

ans = []
queue = deque([])
now = 0
for i in range(N):
    while len(queue) and queue[0] <= i - M:
        j = queue.popleft()
        now -= A[j]
    if now + A[i] <= K:
        ans.append("Yes")
        queue.append(i)
        now += A[i]
    else:
        ans.append("No")


print(*ans, sep="\n")
