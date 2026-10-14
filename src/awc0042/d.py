from collections import defaultdict, deque


N, K = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(deque)
rui = [0 for i in range(N + 1)]

d[0].append(0)
for i in range(N):
    rui[i + 1] = (rui[i] + A[i]) % K
    d[rui[i + 1]].append(i + 1)

ans = 0
for l in range(N):
    d[rui[l]].popleft()
    ans += len(d[rui[l]])
    # print(d.items())

print(ans)
