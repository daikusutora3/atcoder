from collections import defaultdict


N, M = map(int, input().split())
d = defaultdict(int)

for i in range(N):
    A, B = map(int, input().split())
    d[A - 1] -= 1
    d[B - 1] += 1

for i in range(M):
    print(d[i])
