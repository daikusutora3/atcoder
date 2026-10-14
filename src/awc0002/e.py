from bisect import bisect_left, bisect_right
from itertools import combinations


N, S = map(int, input().split())
A = list(map(int, input().split()))

L, R = A[:len(A)//2], A[len(A)//2:]
L_rekkyo = []
R_rekkyo = []
for i in range(len(L)+1):
    for com in list(combinations(L, i)):
        L_rekkyo.append(sum(com))
for i in range(len(R)+1):
    for com in list(combinations(R, i)):
        R_rekkyo.append(sum(com))

L_rekkyo.sort()
R_rekkyo.sort()
ans = 0
for s in L_rekkyo:
    bl = bisect_left(R_rekkyo, S - s)
    br = bisect_right(R_rekkyo, S - s)
    ans += br - bl

print(ans)