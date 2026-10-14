from collections import defaultdict


N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)

for a in A:
    d[a] += a

l = sorted(list(d.items()), key=lambda x: -x[1])
ans = sum(d.values())

for i in range(min(K, len(l))):
    ans -= l[i][1]

print(ans)
