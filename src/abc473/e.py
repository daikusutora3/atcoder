from collections import defaultdict, deque

N, K = map(int, input().split())
A = list(map(int, input().split()))
rui = [0 for i in range(N + 1)]
d = defaultdict(deque)
for i in range(N):
    rui[i + 1] += rui[i] + A[i]
    rui[i + 1] %= K

for i in range(1, N + 1):
    d[rui[i]].append(i)

B = []
for l in range(1, N + 1):
    if len(d[rui[l - 1]]):
        r = d[rui[l - 1]][0]
        B.append((l, r))
    d[rui[l]].popleft()

B.sort(key=lambda x: x[1])
now = -1
ans = 0

for l, r in B:
    if now < l:
        now = r
        ans += 1

print(ans)
