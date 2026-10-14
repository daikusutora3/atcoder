from collections import defaultdict

from sortedcontainers import SortedList


S = input()

d = defaultdict(list)
for i, s in enumerate(S):
    d[s].append(i)

B = SortedList(d["B"])
C = SortedList(d["C"])

ans = 0
for i in d["A"]:
    br = B.bisect_right(i)
    if br < len(B):
        cr = C.bisect_right(B[br])
        if cr < len(C):
            ans += 1
            B.pop(br)
            C.pop(cr)

print(ans)
