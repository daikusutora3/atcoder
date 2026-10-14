from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
d = defaultdict(list)

for i, a in enumerate(A):
    d[a].append(i)

B = [0 for i in range(N)]

cnt = 0
for height in sorted(d.keys(), reverse=True):
    for i in d[height]:
        B[i] = cnt
    cnt += len(d[height])

print(*B)
