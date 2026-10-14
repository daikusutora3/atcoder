from collections import defaultdict


N, M = map(int, input().split())
C = [list(map(int, input().split()))[1:] for i in range(N)]

d = defaultdict(int)
for i in range(N):
    for c in C[i]:
        d[c] += 1

ans = sum([1 if v == N else 0 for v in d.values()])
print(ans)
