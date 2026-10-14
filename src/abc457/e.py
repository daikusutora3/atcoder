from collections import defaultdict

from sortedcontainers import SortedList


N, M = map(int, input().split())
LR = [list(map(int, input().split())) for i in range(M)]
LR.sort(key=lambda x: x[1])

dl = defaultdict(SortedList)
dr = defaultdict(SortedList)

for i in range(M):
    l, r = LR[i]
    dl[l].add((r, i))
    dr[r].add((l, i))

Q = int(input())
ST = [tuple(map(int, input().split())) for _ in range(Q)]
queries = []
for i, (s, t) in enumerate(ST):
    queries.append((s, t, i))

queries.sort(key=lambda x: x[1])
ans = ["No" for i in range(Q)]
now = 0
sorted_l = SortedList()

for _ in range(Q):
    s, t, i = queries[_]
    while now < M and LR[now][1] <= t:
        sorted_l.add(LR[now][0])
        now += 1

    br = dl[s].bisect_right((t, float("inf")))
    bl = dr[t].bisect_left((s, -float("inf")))
    if 0 <= br - 1 < len(dl[s]) and 0 <= bl < len(dr[t]):
        l_nuno = dl[s][br - 1]
        r_nuno = dr[t][bl]
        if r_nuno[0] <= l_nuno[0] + 1:
            # 2枚の布を組み合わせていける
            if l_nuno[1] != r_nuno[1]:
                ans[i] = "Yes"
            # 1枚の布で覆ってしまって、もう1枚はそれに完全に乗る布
            elif len(sorted_l) - sorted_l.bisect_left(s) >= 2:
                ans[i] = "Yes"

print(*ans, sep="\n")
