from collections import defaultdict


N, M, T = map(int, input().split())

d = defaultdict(list)

for i in range(M):
    c, s = map(int, input().split())
    d[c].append(s)

ans = 0
for v in d.values():
    if sum(v) / len(v) < T:
        ans += 1

print(ans)
