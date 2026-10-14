import bisect
from collections import deque

from sortedcontainers import SortedList

N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort()
B.sort()

H = deque(H)
B = SortedList(B)
ans = "Yes"
for _ in range(K):
    h = H.popleft()
    a = bisect.bisect_left(B, h, 0, len(B))
    if a == len(B):
        ans = "No"
        break
    B.remove(B[a])
    # print(a, B[a])

print(ans)
