from sortedcontainers import SortedList
from collections import deque


N = int(input())
HL = [list(map(int, input().split())) for _ in range(N)]
HL.sort(key=lambda x: x[1])
HL = deque(HL)
sl = SortedList()
for h, _ in HL:
    sl.add(h)

Q = int(input())
T = list(map(int, input().split()))
queries = []
for i, t in enumerate(T):
    queries.append((t, i))

queries.sort()
ans = [-1 for i in range(Q)]


for t, i in queries:
    while HL[0][1] <= t:
        h, _ = HL.popleft()
        # print(sl, h)
        sl.remove(h)
    ans[i] = sl[-1]

print(*ans, sep="\n")
