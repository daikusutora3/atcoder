from bisect import bisect_left, bisect_right
from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(int)
for a in A:
    d[a] += 1

B = []

for v in d.values():
    B.append(v)  # noqa: PERF402

B.sort()
print(bisect_right(B, B[-1]) - bisect_left(B, B[-1] - 1))
