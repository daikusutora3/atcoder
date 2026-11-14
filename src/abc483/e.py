from collections import defaultdict
from itertools import combinations

N, M = map(int, input().split())

d = defaultdict(int)

comb_res = []
for cnt in range(3):
    comb_res.append(list(combinations(range(M), cnt)))

for _ in range(N):
    S = input()
    res = list(S)
    for cnt in range(3):
        for com in comb_res[cnt]:
            for i in com:
                res[i] = "*"
            d["".join(res)] += 1
            for i in com:
                res[i] = S[i]

ans = 0
for k in d:
    if k.count("*") == 2:
        ans += d[k] * (d[k] - 1) // 2
    elif k.count("*") == 1:
        ans -= (M - 2) * d[k] * (d[k] - 1) // 2
    else:
        ans += ((M - 1) * (M - 2) // 2) * d[k] * (d[k] - 1) // 2

print(ans)
