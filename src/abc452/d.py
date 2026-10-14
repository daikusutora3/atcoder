from bisect import bisect_left
from collections import defaultdict

S = input()
T = input()

d = defaultdict(list)
for i, s in enumerate(S):
    d[s].append(i)

ans = 0
for l in range(len(S)):
    r = l - 1
    for t in T:
        bl = bisect_left(d[t], r + 1)
        if len(d[t]) > bl:
            r = d[t][bl]
        else:
            r = len(S)
    ans += r - l

print(ans)
