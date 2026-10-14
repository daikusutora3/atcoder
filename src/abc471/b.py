from collections import defaultdict

N = int(input())
d = defaultdict(int)

for i in range(N):
    S = input()
    d[S.lower()] += 1

print(max(d.values()))
