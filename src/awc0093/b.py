from collections import deque


N = int(input())
P = list(map(int, input().split()))

ans = [0 for i in range(N)]
queue = deque([0])
ans[0] = 1

while len(queue):
    v = queue.popleft()
    nv = P[v] - 1
    if ans[nv]:
        pass
    else:
        queue.append(nv)
        ans[nv] = 1

print(sum(ans))
