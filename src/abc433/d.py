from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(dict)

for a in A:
    for digits in range(1, 11):
        a_mod = (a * (10**digits)) % M
        if a_mod in d[digits]:
            d[digits][a_mod] += 1
        else:
            d[digits][a_mod] = 1

ans = 0
for a in A:
    mod = M - a % M if a % M else 0
    if mod in d[len(str(a))]:
        ans += d[len(str(a))][mod]

print(ans)
