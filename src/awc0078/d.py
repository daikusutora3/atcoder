from collections import defaultdict
from heapq import heapify, heappop
from atcoder.dsu import DSU

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]

hq = [(a, i, b) for i, (a, b) in enumerate(AB)]
heapify(hq)

dsu = DSU(N)

# dsuの各合体された集合のleaderに対して、その集合の重量の最大値を持っておく
d = dict()
for i in range(N):
    d[i] = 0

query = [[int(input()), i] for i in range(Q)]
query.sort()


ans = [-1 for i in range(Q)]

ANS = 0
# 基準値kを小さい順に取ってくる
# _番目のquery
for k, _ in query:
    # hq[0][0]まだ箱に入れていない、商品の中で品質が一番小さいもの
    while len(hq) and hq[0][0] < k:
        a, i, b = heappop(hq)
        li = i - 1
        ri = i + 1
        res = AB[i][1]
        if li >= 0 and AB[li][0] <= AB[i][0]:
            ANS -= d[dsu.leader(li)]
            res = max(res, d[dsu.leader(li)])
            dsu.merge(li, i)
        if ri < N and AB[ri][0] < AB[i][0]:
            ANS -= d[dsu.leader(ri)]
            res = max(res, d[dsu.leader(ri)])
            dsu.merge(ri, i)
        # print(ANS)
        d[dsu.leader(i)] = res
        ANS += d[dsu.leader(i)]
        # print(dsu.groups(), ANS)
    ans[_] = ANS

print(*ans, sep="\n")
