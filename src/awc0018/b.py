from collections import defaultdict


N, M = map(int, input().split())
C = list(map(int, input().split()))

ans = 0

for _ in range(N):
    K = int(input())
    P = list(map(int, input().split()))
    CNT = defaultdict(int)
    for i in range(K):
        CNT[P[i] - 1] += 1
    for k in CNT.keys():
        if CNT[k] <= C[k]:
            ans += CNT[k]

print(ans)
