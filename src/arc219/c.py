from collections import defaultdict

H, W = map(int, input().split())
N = int(input())
AB = [list(map(int, input().split())) for i in range(N)]
d = defaultdict(list)
d_dm = defaultdict(int)
for i, (a, b) in enumerate(AB):
    d[a].append(b)


keys = list(d.keys())
for k in keys:
    for i in range(d[k]):
        d_dm[k] = max(d_dm[k], abs(d[k][i] - d[k][i]))

ans1 = 0
for k in keys:
    ans1 += d[k][-1] * 2


ans2 = max(d_dm.values()) + W
