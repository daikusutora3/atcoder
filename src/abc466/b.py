from collections import defaultdict


N, M = map(int, input().split())
d = defaultdict(lambda: -1)

for _ in range(N):
    C, S = map(int, input().split())
    d[C] = max(d[C], S)

for i in range(1, M + 1):
    print(d[i])
