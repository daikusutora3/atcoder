from collections import defaultdict

N = int(input())

d = defaultdict(int)
A = list(map(int, input().split()))

for a in A:
    d[a] += 1

ans = 0
for k, v in d.items():
    ans += k * (v % 2)

print(ans)
