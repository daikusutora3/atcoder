from collections import defaultdict
from math import comb


N = int(input())
S = input()

ans = comb(N + 1, 2)

rA = [0 for i in range(N + 1)]
rB = [0 for i in range(N + 1)]
rC = [0 for i in range(N + 1)]

for i, s in enumerate(S):
    rA[i + 1] += rA[i] + (1 if s == "A" else 0)
    rB[i + 1] += rB[i] + (1 if s == "B" else 0)
    rC[i + 1] += rC[i] + (1 if s == "C" else 0)


def f(rd):
    d = defaultdict(int)
    res = 0
    for a in rd:
        d[a] += 1

    for v in d.values():
        if v >= 2:
            res += comb(v, 2)
    return res


rd = [rA[i] - rB[i] for i in range(N + 1)]
ans -= f(rd)
rd = [rA[i] - rC[i] for i in range(N + 1)]
ans -= f(rd)
rd = [rB[i] - rC[i] for i in range(N + 1)]
ans -= f(rd)


rdAB = [rA[i] - rB[i] for i in range(N + 1)]
rdAC = [rA[i] - rC[i] for i in range(N + 1)]
d = defaultdict(int)
for i in range(N + 1):
    d[(rdAB[i], rdAC[i])] += 1
for v in d.values():
    if v >= 2:
        ans += 2 * comb(v, 2)
print(ans)
