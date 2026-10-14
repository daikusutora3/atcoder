from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
MAX = max(A)
d = defaultdict(list)
ans = 0
for i, a in enumerate(A):
    d[a].append(i)
    if a % 5 == 0:
        ans += len(d[(a // 5) * 7]) * len(d[(a // 5) * 3])

d = defaultdict(list)
for i, a in enumerate(A[::-1]):
    d[a].append(i)
    if a % 5 == 0:
        ans += len(d[(a // 5) * 7]) * len(d[(a // 5) * 3])

print(ans)
