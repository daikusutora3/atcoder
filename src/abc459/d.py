from collections import defaultdict
from heapq import heappop, heappush


T = int(input())

for _ in range(T):
    S = input()
    d = defaultdict(int)
    for s in S:
        d[s] += 1
    if max(d.values()) > len(S) // 2 + (1 if len(S) % 2 == 1 else 0):
        print("No")
        continue
    hq = []
    for k, v in d.items():
        heappush(hq, [-v, k])
    ans = []
    while len(hq):
        v, k = heappop(hq)
        v = -v
        ans.append(k)
        if v - 1 == 0:
            continue
        hq.append([-(v - 1), k])
    print("Yes")
    print("".join(ans))
