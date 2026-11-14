from collections import defaultdict
from itertools import combinations

N, M = map(int, input().split())

d = defaultdict(int)

comb_res = []
for cnt in range(3):
    comb_res.append(list(combinations(range(M), cnt)))

# ここまでは元のコードと同じ
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


# g[mask] = 異なる位置がmaskの部分集合であるペア数
g = [0] * (1 << M)

for k, v in d.items():
    mask = 0
    for i in range(M):
        if k[i] == "*":
            mask |= 1 << i

    g[mask] += v * (v - 1) // 2


# 集合のメビウス変換
# f[mask] = 異なる位置がちょうどmaskであるペア数
f = g[:]

for i in range(M):
    for mask in range(1 << M):
        if mask & (1 << i):
            f[mask] -= f[mask ^ (1 << i)]


# ハミング距離2以下のペアを数える
ans = 0
for mask in range(1 << M):
    if mask.bit_count() <= 2:
        ans += f[mask]

print(ans)
