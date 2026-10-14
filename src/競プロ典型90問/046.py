from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_d = defaultdict(int)
B_d = defaultdict(int)
C_d = defaultdict(int)

for i in range(N):
    A_d[A[i] % 46] += 1
    B_d[B[i] % 46] += 1
    C_d[C[i] % 46] += 1

ans = 0
for a in range(46):
    for b in range(46):
        c = (46 - a - b) % 46
        ans += A_d[a] * B_d[b] * C_d[c]

print(ans)
